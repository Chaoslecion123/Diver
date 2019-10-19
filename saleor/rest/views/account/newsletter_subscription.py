from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import NewsletterSubscriptionSerializer


__all__ = [
    'NewsletterSubscriptionViewSet',
]

NewsletterSubscription = apps.get_model(*'account.NewsletterSubscription'.split())


class NewsletterSubscriptionViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`account.NewsletterSubscription`

    `** Actions **`:

    create:
    Create a new `account.NewsletterSubscription` instance.

    retrieve:
    Return the given `account.NewsletterSubscription`.

    update:
    Update the given `account.NewsletterSubscription`..

    delete:
    Delete the given `account.NewsletterSubscription`, and return an empty response 
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`NewsletterSubscription`.
    """

    lookup_field = 'id'
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'customer', # [account.User]
        # 'email',
        # 'id',
        # 'is_active',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'customer',
        # 'email',
        # 'id',
        # 'is_active',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'customer',
        # 'email',
        # 'id',
        # 'is_active',

        # Reverse Fields
    ] 
    # '__all__'

    # def get_object(self):
    #     return super().get_object()

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #    return super().update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
