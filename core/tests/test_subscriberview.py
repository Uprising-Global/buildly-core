from django.test import TestCase
import factories
from rest_framework.test import APIRequestFactory

from core.views import SubscriberViewSet


class SubscriberListViewTest(TestCase):
    def setUp(self):
        factories.Subscriber.create()
        factories.Subscriber.create(email='test@example.com')

        factory = APIRequestFactory()
        self.request = factory.get('/subscriber/')

    def test_list_subscribers(self):
        view = SubscriberViewSet.as_view({'get': 'list'})
        response = view(self.request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
