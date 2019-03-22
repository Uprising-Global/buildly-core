# Generated by Django 2.0.7 on 2019-03-14 09:51

import django.contrib.auth.validators
from django.db import migrations, models
from workflow.models import CoreUser


def forwards(apps, schema_editor):
    for core_user in CoreUser.objects.all():
        user = core_user.user
        core_user.username = user.username
        core_user.first_name = user.first_name
        core_user.last_name = user.last_name
        core_user.email = user.email
        core_user.is_staff = user.is_staff
        core_user.is_active = user.is_active
        core_user.is_superuser = user.is_superuser
        core_user.last_login = user.last_login
        core_user.password = user.password
        core_user.date_joined = user.date_joined
        core_user.save()

        core_user.user_permissions.add(*list(user.user_permissions.all()))


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0010_coreuser_is_active'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
        migrations.AlterField(
            model_name='coreuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
