from django.apps import apps
from django.db.models import Q
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet

from ...serializers import AddressSerializer
from ...permissions import ReadOnly


__all__ = [
    'AddressViewSet',
]

Address = apps.get_model(*'account.Address'.split())


class AddressViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`account.Address`

    `** Actions **`:

    create:
    Create a new `account.Address` instance.

    retrieve:
    Return the given `account.Address`.

    update:
    Update the given `account.Address`..

    delete:
    Delete the given `account.Address`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Address`.
    """

    permission_classes = [ReadOnly]
    lookup_field = 'id'
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'city',
        # 'city_area',
        # 'company_name',
        # 'country',
        # 'country_area',
        # 'first_name',
        # 'id',
        # 'last_name',
        # 'phone',
        # 'postal_code',
        # 'street_address_1',
        # 'street_address_2',
        # 'country_area_object',
        # 'city_object',
        # 'city_area_object',

        # Reverse Fields
        # 'user_addresses',
    ]
    search_fields = [
        # Fields
        # 'city',
        # 'city_area',
        # 'company_name',
        # 'country',
        # 'country_area',
        # 'first_name',
        # 'id',
        # 'last_name',
        # 'phone',
        # 'postal_code',
        # 'street_address_1',
        # 'street_address_2',
        # 'country_area_object',
        # 'city_object',
        # 'city_area_object',

        # Reverse Fields
        # 'user_addresses',
    ]
    ordering_fields = [
        # Fields
        # 'city',
        # 'city_area',
        # 'company_name',
        # 'country',
        # 'country_area',
        # 'first_name',
        # 'id',
        # 'last_name',
        # 'phone',
        # 'postal_code',
        # 'street_address_1',
        # 'street_address_2',
        # 'country_area_object',
        # 'city_object',
        # 'city_area_object',

        # Reverse Fields
        # 'user_addresses',
    ]
    # '__all__'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.request.user.addresses.all()

        lookup_expr = Q()

        id_ = self.kwargs.get('id', None)

        if id_:
            lookup_expr = lookup_expr | Q(id=id_)

        if lookup_expr.children:
            return super().get_queryset().filter(lookup_expr)

        return Address.objects.none()

    def create(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            address = Address.objects.get(id=serializer.data['id'])
            request.user.addresses.add(address)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return super().create(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #    return super().update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
