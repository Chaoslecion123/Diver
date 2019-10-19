from django.apps import apps
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from saleor.rest.serializers import SliderSerializer
from ....widget import SliderType
from ...permissions import ReadOnly


__all__ = [
    'SliderViewSet',
]

#Slider = apps.get_model(*'homepage.Slider'.split())
Slider = apps.get_model(*'widget.Slider'.split())


class SliderViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`homepage.Slider`

    `** Actions **`:

    create:
    Create a new `homepage.Slider` instance.

    retrieve:
    Return the given `homepage.Slider`.

    update:
    Update the given `homepage.Slider`..

    delete:
    Delete the given `homepage.Slider`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Slider`.
    """
    permission_classes = [ReadOnly]
    lookup_field = 'id'
    permit_list_expands = ['slides']
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'type',
        # 'name',
        'is_active',
        # 'active_on',
        # 'active_until',
        'is_default',
        # 'collections',
        # 'categories',
        # 'brands',

        # Reverse Fields
        # 'slides',
    ]
    search_fields = [
        # Fields
        # 'type',
        # 'name',
        # 'is_active',
        # 'active_on',
        # 'active_until',
        # 'is_default',
        # 'collections',
        # 'categories',
        # 'brands',

        # Reverse Fields
        # 'slides',
    ]
    ordering_fields = [
        # Fields
        # 'type',
        # 'name',
        # 'is_active',
        # 'active_on',
        # 'active_until',
        # 'is_default',
        # 'collections',
        # 'categories',
        # 'brands',

        # Reverse Fields
        # 'slides',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_expanded(self.request, 'slides'):
            queryset = queryset.prefetch_related('slides')
        return queryset

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
    def home_page_slider(self, request, *args, **kwargs):
        sliders = Slider.objects.filter(type=SliderType.HOMEPAGE)
        slider = sliders.filter(is_active=True).first()

        if slider is None:
            slider = sliders.filter(is_default=True).first()

        if slider is None:
            return Response({"detail": "No encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serialized_slider = SliderSerializer(
            slider,
            expand=['slides']
        )

        return Response(serialized_slider.data)
