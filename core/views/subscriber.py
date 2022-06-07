import logging

import django_filters
from django.shortcuts import get_object_or_404
from core.models import Subscriber
from core.serializers import SubscriberSerializer
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


logger = logging.getLogger(__name__)


class SubscriberViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    Subscribers is a collection of emails that want to be notified about updates from Uprising.

    title:
    Subscribers is a collection of emails.

    description:
    Subscribers is a collection of emails that want to be notified about updates (newsletter, promotion emails, etc.)
    from from Uprising.

    list:
    Return a list of all the subscribers.
    """

    def list(self, request, *args, **kwargs):
        # Use this queryset or the django-filters lib will not work
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(
            instance=queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.queryset
        subscriber = get_object_or_404(queryset, pk=kwargs.get('pk'))
        serializer = self.get_serializer(instance=subscriber, context={'request': request})
        return Response(serializer.data)

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    permission_classes = (AllowAny,)
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
