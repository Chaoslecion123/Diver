from django import template

from ...product.templatetags.product_images import get_thumbnail

register = template.Library()


@register.simple_tag()
def get_brand_logo_image_thumbnail(instance, size, method):
    image_file = None
    if instance and instance.logo_image:
        image_file = instance.logo_image
    return get_thumbnail(image_file, size, method, rendition_key_set="brands")
