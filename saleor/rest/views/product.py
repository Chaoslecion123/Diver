from django.apps import apps
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet

from saleor.checkout.utils import set_checkout_cookie
from saleor.product.utils import (
    handle_checkout_form, products_for_products_list, products_with_details)
from saleor.rest.serializers import ProductSerializer
from saleor.search.forms import SearchForm

from ..serializers import CheckoutSerializer
# from ..permissions import ReadOnly


__all__ = [
    'ProductViewSet',
]

Product = apps.get_model(*'product.Product'.split())


class ProductElasticSearch(SearchFilter):
    def filter_queryset(self, request, queryset, view):
        form = SearchForm(data=request.GET or None)
        if form.is_valid():
            query = form.cleaned_data.get(self.search_param, '')
            # results = evaluate_search_query(form, request)
            results = products_with_details(request.user) & form.search()
        else:
            query, results = '', queryset

        page = list(results)

        return results  # super().filter_queryset(request, queryset, view)


class ProductViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`product.Product`

    `** Actions **`:

    create:
    Create a new `product.Product` instance.

    retrieve:
    Return the given `product.Product`.

    update:
    Update the given `product.Product`..

    delete:
    Delete the given `product.Product`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Product`.
    """
    # permission_classes = (ReadOnly,)
    # parser_classes = (JSONParser,)

    lookup_field = 'id'
    permit_list_expands = ['images']

    # Just get availabvle products with get_queryset function
    # queryset = Product.objects.available_products()
    queryset = Product.objects.all()

    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    # filter_backends = [DjangoFilterBackend, ProductElasticSearch, OrderingFilter, ]

    filter_fields = [
        # Fields
        'category',  # [product.Category]
        'collections',  # [product.Collection]
        'attributes',
        # 'available_on',
        # 'charge_taxes',
        # 'description',
        # 'id',
        # 'is_published',
        # 'name',
        # 'price',
        # 'product_type', # [product.ProductType]
        # 'seo_description',
        # 'seo_title',
        # 'tax_rate',
        # 'updated_at',
        # 'weight',
        # 'video',
        # 'related_products',

        # Reverse Fields
        # 'images',
        # 'sale',
        # 'translations',
        # 'variants',
        # 'voucher',
    ]
    search_fields = [
        # Fields
        # 'attributes',
        # 'available_on',
        # 'category',
        # 'charge_taxes',
        # 'description',
        # 'id',
        # 'is_published',
        'name',
        # 'price',
        # 'product_type',
        # 'seo_description',
        # 'seo_title',
        # 'tax_rate',
        # 'updated_at',
        # 'weight',
        # 'video',
        # 'related_products',

        # Reverse Fields
        # 'collections',
        # 'images',
        # 'sale',
        # 'translations',
        # 'variants',
        # 'voucher',
    ]

    ordering_fields = [
        # Fields
        # 'attributes',
        # 'available_on',
        # 'category',
        # 'charge_taxes',
        # 'description',
        # 'id',
        # 'is_published',
        # 'name',
        # 'price',
        # 'product_type',
        # 'seo_description',
        # 'seo_title',
        # 'tax_rate',
        # 'updated_at',
        # 'weight',
        # 'video',
        # 'related_products',

        # Reverse Fields
        # 'collections',
        # 'images',
        # 'sale',
        # 'translations',
        # 'variants',
        # 'voucher',
    ]
    # '__all__'

    def get_queryset(self):
        return products_for_products_list(self.request.user)

    # def get_object(self):
    #     return super().get_object()

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #    return super().update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=['post'],
        detail=True,
        name='add-to-checkout',
        url_path='add-to-checkout',
        url_name='add-to-checkout'
    )
    def add_to_checkout(self, request, *args, **kwargs):
        response_data = {
            'token': None,
            'errors': None,
        }

        instance = self.get_object()
        form, checkout = handle_checkout_form(
            request, instance, create_checkout=True)

        if form.is_valid():
            form.save()

            if request.user.is_authenticated:
                if request.user != checkout.user:
                    checkout.user = request.user

            if not request.user.is_authenticated:
                checkout.user = None

            checkout.save()

            response_data['token'] = checkout.token

            response = Response(response_data)
        else:
            response_data['errors'] = form.error_messages
            response = Response(response_data, status=400)

        if not request.user.is_authenticated:
            set_checkout_cookie(checkout, response)

        return response
