from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'PageSerializer',
]

Page = apps.get_model(*'page.Page'.split())


class PageSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`page.Page`:

    `**Fields:**`
        01. `available_on`                : `DateField`
        02. `content`                     : `TextField`
        03. `created`                     : `DateTimeField`
        04. `id`                          : `AutoField`
        05. `is_visible`                  : `BooleanField`
        06. `seo_description`             : `CharField`
        07. `seo_title`                   : `CharField`
        08. `slug`                        : `SlugField`
        09. `title`                       : `CharField`

    `**Reverse Fields:**`
        01. `menuitem`                    : `ForeignKey` [:model:`menu.MenuItem`]
        02. `translations`                : `ForeignKey` [:model:`page.PageTranslation`]
    """
    class Meta:
        model = Page
        fields = [
            # Fields
            # 'available_on',
            'publication_date',
            'content',
            'created',
            'id',
            'is_visible',
            'seo_description',
            'seo_title',
            'slug',
            'title',

            # Reverse Fields
            # 'menuitem',
            # 'translations',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
