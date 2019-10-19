from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer




__all__ = [
    'BannerSerializer',
]

Banner = apps.get_model(*'widget.Banner'.split())


class BannerSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`widget.Banner`:

    `**Fields:**`
        01. `active_on`                   : `DateField`
        02. `active_until`                : `DateField`
        03. `alt`                         : `CharField`
        04. `id`                          : `AutoField`
        05. `image`                       : `FileField`
        06. `is_active`                   : `BooleanField`
        07. `is_default`                  : `BooleanField`
        08. `name`                        : `CharField`
        09. `ppoi`                        : `CharField`

    `**Reverse Fields:**`
    """
    image = VersatileImageFieldSerializer(
        sizes=(('original', 'url'), )
    )

    class Meta:
        model = Banner
        fields = [
            # Fields
            'id',
            'alt',
            'name',
            'image',
            # 'active_on',
            # 'active_until',
            # 'is_active',
            # 'is_default',
            # 'ppoi',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
