from django.apps import apps
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny
)

from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet

from saleor.checkout.utils import set_checkout_cookie
from saleor.product.utils import handle_checkout_form, products_for_products_list
from saleor.rest.serializers import ProductSerializer
from saleor.search.forms import SearchForm
from saleor.product.filters import ProductFilter

from ...serializers import ProductSerializer
from ...permissions import ReadOnly


__all__ = [
    'ProductViewSet',
]

Brand = apps.get_model(*'brand.Brand'.split())
Product = apps.get_model(*'product.Product'.split())
Category = apps.get_model(*'product.Category'.split())
Collection = apps.get_model(*'product.Collection'.split())
Favorite = apps.get_model(*'favorites.Favorite'.split())


class ProductViewSetFilter(ProductFilter):
    category = None
    collection = None
    brand = None

    def __init__(self, *args, **kwargs):
        request = kwargs.get('request', None)
        if request is not None:
            self.category = request.GET.get('category', None)
            self.collection = request.GET.get('collection', None)
            self.brand = request.GET.get('brand', None)

        if self.category is not None:
            self.category = get_object_or_404(Category, id=self.category)

        if self.collection is not None:
            self.collection = get_object_or_404(Collection, id=self.collection)

        if self.brand is not None:
            self.brand = get_object_or_404(Brand, id=self.brand)

        super().__init__(*args, **kwargs)

    def _get_product_attributes_lookup(self):
        if self.brand is not None:
            return Q(product_type__products__brand=self.brand)

        if self.collection is not None:
            return Q(product_type__products__collections=self.collection)

        if self.category is not None:
            categories = self.category.get_descendants(include_self=True)
            return Q(product_type__products__category__in=categories)

        return Q()

    def _get_variant_attributes_lookup(self):
        if self.brand is not None:
            return Q(product_variant_type__products__brand=self.collection)

        if self.collection is not None:
            return Q(product_variant_type__products__collections=self.collection)

        if self.category is not None:
            categories = self.category.get_descendants(include_self=True)
            return Q(product_variant_type__products__category__in=categories)

        return Q()


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
    permission_classes = (ReadOnly, )
    # parser_classes = (JSONParser,)
    # http_method_names = ['get', 'head', 'options']

    lookup_field = 'id'
    permit_list_expands = ['images', 'brand', ]

    # Just get availabvle products with get_queryset function
    # queryset = Product.objects.available_products()
    queryset = Product.objects.all()

    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_class = ProductViewSetFilter
    filter_fields = [
        # Fields
        'category',  # [product.Category]
        'collections',  # [product.Collection]
        # 'attributes',
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
        'brand',
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
        qs = products_for_products_list(self.request.user)
        category = self.request.GET.get('category', None)
        collection = self.request.GET.get('collection', None)
        brand = self.request.GET.get('brand', None)

        if category is not None:
            return qs.filter(category=category)

        if collection is not None:
            return qs.filter(collection=collection)

        if brand is not None:
            return qs.filter(brand=brand)

        return qs

    # def get_object(self):
    #     return super().get_object()

    def get_permissions(self):
        permission_classes = [ReadOnly]

        open_actions = [
            'add_to_checkout'
        ]
        if self.action in open_actions:
            permission_classes = [AllowAny]

        auth_required_actions = [
            'add_to_favorites',
            'remove_from_favorites'
        ]
        if self.action in auth_required_actions:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

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
            response_data['errors'] = {}
            for field in form:
                if field.errors:
                    response_data['errors'][field.name] = field.errors  # pylint: disable=unsupported-assignment-operation

            response = Response(
                response_data, status=status.HTTP_400_BAD_REQUEST)

        if not request.user.is_authenticated:
            set_checkout_cookie(checkout, response)

        return response

    @action(
        methods=['post'],
        detail=True,
        name='add-to-favorites',
        url_path='add-to-favorites',
        url_name='add-to-favorites'
    )
    def add_to_favorites(self, request, *args, **kwargs):
        response_data = {
            'detail': 'Not authenticated user.',
            'code': 'not-authenticated'
        }
        response_status = status.HTTP_400_BAD_REQUEST

        product = self.get_object()
        user = self.request.user

        if user.is_authenticated:
            _, created = Favorite.objects.get_or_create(
                product=product,
                user=user,
                defaults={
                    'product': product,
                    'user': user,
                }
            )

            response_data = {
                'user': user.pk,
                'product': ProductSerializer(product).data,
            }

            if created:
                response_status = status.HTTP_201_CREATED
            else:
                # response_status = status.HTTP_304_NOT_MODIFIED
                response_status = status.HTTP_200_OK

        return Response(response_data, status=response_status)

    @action(
        methods=['post'],
        detail=True,
        name='remove-from-favorites',
        url_path='remove-from-favorites',
        url_name='remove-from-favorites'
    )
    def remove_from_favorites(self, request, *args, **kwargs):
        response_data = {
            'detail': 'Not authenticated user.',
            'code': 'not-authenticated'
        }

        response_status = status.HTTP_400_BAD_REQUEST

        product = self.get_object()
        user = self.request.user

        if user.is_authenticated:
            favorite = Favorite.objects.filter(
                product=product,
                user=user
            ).first()

            if favorite:
                try:
                    favorite.delete()
                    response_data = {}
                    response_status = status.HTTP_204_NO_CONTENT
                except Exception as msg:  # pylint: disable=broad-except
                    response_data = {
                        'detail': msg,
                        'code': 'bad-operation'
                    }
            else:
                response_data = {
                    'detail': 'This product is not favorite.',
                    'code': 'not-favorite'
                }

        return Response(response_data, status=response_status)
