from django.apps import apps
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import UserSerializer

from ...permissions import ReadOnly



__all__ = [
    'UserViewSet',
]

User = apps.get_model(*'account.User'.split())


class UserViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`account.User`

    `** Actions **`:

    create:
    Create a new `account.User` instance.

    retrieve:
    Return the given `account.User`.

    update:
    Update the given `account.User`..

    delete:
    Delete the given `account.User`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`User`.
    """
    permission_classes = [ReadOnly]
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'addresses', # [account.Address]
        # 'date_joined',
        # 'default_billing_address', # [account.Address]
        # 'default_shipping_address', # [account.Address]
        # 'email',
        # 'first_name',
        # 'groups', # [auth.Group]
        # 'id',
        # 'is_active',
        # 'is_staff',
        # 'is_superuser',
        # 'last_login',
        # 'last_name',
        # 'note',
        # 'password',
        # 'token',
        # 'user_permissions', # [auth.Permission]

        # Reverse Fields
        # 'auth_token',
        # 'checkouts',
        # 'customernote',
        # 'impersonated_by',
        # 'impersonations',
        # 'logentry',
        # 'notes',
        # 'orders',
        # 'social_auth',
    ]
    search_fields = [
        # Fields
        # 'addresses',
        # 'date_joined',
        # 'default_billing_address',
        # 'default_shipping_address',
        # 'email',
        # 'first_name',
        # 'groups',
        # 'id',
        # 'is_active',
        # 'is_staff',
        # 'is_superuser',
        # 'last_login',
        # 'last_name',
        # 'note',
        # 'password',
        # 'token',
        # 'user_permissions',

        # Reverse Fields
        # 'auth_token',
        # 'checkouts',
        # 'customernote',
        # 'impersonated_by',
        # 'impersonations',
        # 'logentry',
        # 'notes',
        # 'orders',
        # 'social_auth',
    ]
    ordering_fields = [
        # Fields
        # 'addresses',
        # 'date_joined',
        # 'default_billing_address',
        # 'default_shipping_address',
        # 'email',
        # 'first_name',
        # 'groups',
        # 'id',
        # 'is_active',
        # 'is_staff',
        # 'is_superuser',
        # 'last_login',
        # 'last_name',
        # 'note',
        # 'password',
        # 'token',
        # 'user_permissions',

        # Reverse Fields
        # 'auth_token',
        # 'checkouts',
        # 'customernote',
        # 'impersonated_by',
        # 'impersonations',
        # 'logentry',
        # 'notes',
        # 'orders',
        # 'social_auth',
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

    @action(
        methods=['post'],
        detail=False,
        name='verify',
        url_path='verify',
        url_name='verify'
    )
    def verify(self, request, *args, **kwargs):
        response_status = status.HTTP_404_NOT_FOUND
        response_data = {
            'exists': False,
        }
        email = request.data.get('email', None)

        if email:
            response_data['exists'] = User.objects.filter(email=email).exists()

        if response_data['exists']:
            response_status = status.HTTP_200_OK

        response = Response(response_data, status=response_status)

        return response
