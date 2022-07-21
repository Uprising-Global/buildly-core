from django.conf import settings

from google.cloud import storage
from google.oauth2 import service_account

def upload_to_cloud(imported_file, filename):
    # Use service account credentials to authenticate Cloud Storage
    credentials = service_account.Credentials.from_service_account_info(
        settings.CREDENTIALS_DICT
    )
    client = storage.Client(project=settings.GCP_PROJECT, credentials=credentials)

    # Get the required bucket
    bucket = client.get_bucket(settings.GCP_CLOUD_STORAGE)
    blob = bucket.blob('avatar/' + filename)
    blob.upload_from_file(imported_file.file, rewind=True)  # Uploads file to Bucket
    blob.make_public()

    blob.content_disposition = 'inline'
    import mimetypes

    blob.content_type = mimetypes.guess_type(filename)
    blob.patch()

    return blob.public_url


def delete_from_cloud(filename):
    # Use service account credentials to authenticate Cloud Storage
    credentials = service_account.Credentials.from_service_account_info(
        settings.CREDENTIALS_DICT
    )
    client = storage.Client(project=settings.GCP_PROJECT, credentials=credentials)

    # Get the required bucket
    bucket = client.get_bucket(settings.GCP_CLOUD_STORAGE)
    blob = bucket.blob('avatar/' + filename)
    blob.delete()
