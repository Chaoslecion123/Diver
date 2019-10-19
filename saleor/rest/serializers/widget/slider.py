from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer


from .slide import SlideSerializer


__all__ = [
    'SliderSerializer',
]

Slider = apps.get_model(*'widget.Slider'.split())
Slide = apps.get_model(*'widget.Slide'.split())


class SliderSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`widget.Slider`:

    `**Fields:**`
        01. `active_on`                   : `DateField`
        02. `active_until`                : `DateField`
        03. `brands`                      : `ManyToManyField` [:model:`brand.Brand`]
        04. `categories`                  : `ManyToManyField` [:model:`product.Category`]
        05. `collections`                 : `ManyToManyField` [:model:`product.Collection`]
        06. `id`                          : `AutoField`
        07. `is_active`                   : `BooleanField`
        08. `is_default`                  : `BooleanField`
        09. `name`                        : `CharField`
        10. `type`                        : `CharField`

    `**Reverse Fields:**`
        01. `slides`                      : `ForeignKey` [:model:`widget.Slide`]
    """
    slides = serializers.PrimaryKeyRelatedField(
        queryset=Slide.objects.all(),
        allow_null=False,
        required=False,
        many=True,
    )

    expandable_fields = {
        'slides': (
            SlideSerializer, {
                'fields': [
                    'id',
                    'alt',
                    'image',
                    'sort_order',
                ],
                'many': True
            }
        )
    }

    class Meta:
        model = Slider
        fields = [
            # Fields
            'id',
            'type',
            # 'active_on',
            # 'active_until',
            # 'brands',
            # 'categories',
            # 'collections',
            # 'is_active',
            # 'is_default',
            # 'name',

            # Reverse Fields
            'slides',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
