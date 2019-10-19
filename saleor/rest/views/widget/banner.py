from django.apps import apps
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import BannerSerializer
from ...permissions import ReadOnly


__all__ = [
    'BannerViewSet',
]

Banner = apps.get_model(*'widget.Banner'.split())


class BannerViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`widget.Banner`

    `** Actions **`:

    create:
    Create a new `widget.Banner` instance.

    retrieve:
    Return the given `homepage.Banner`.

    update:
    Update the given `homepage.Banner`..

    delete:
    Delete the given `homepage.Banner`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Banner`.
    """

    permission_classes = [ReadOnly]
    lookup_field = 'id'
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'active',
        # 'id',
        # 'image',
        # 'name',
        # 'ppoi',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'active',
        # 'id',
        # 'image',
        # 'name',
        # 'ppoi',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'active',
        # 'id',
        # 'image',
        # 'name',
        # 'ppoi',

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

    @action(
        methods=['get'],
        detail=False,
        name='homepage',
        url_path='homepage',
        url_name='homepage'
    )
    def home_page_banner(self, request, *args, **kwargs):
        banners = Banner.objects.all()
        banner = banners.filter(is_active=True).first()

        if banner is None:
            banner = banners.filter(is_default=True).first()

        if banner is None:
            return Response({"detail": "No encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serialized_banner = BannerSerializer(
            banner,
            expand=['slides']
        )

        return Response(serialized_banner.data)
