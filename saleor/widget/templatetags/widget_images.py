from django import template

from ...product.templatetags.product_images import get_thumbnail

register = template.Library()


@register.simple_tag()
def get_benefit_thumbnail(instance, size, method):
    image_file = None
    if instance and instance.image:
        image_file = instance.image
    return get_thumbnail(image_file, size, method, rendition_key_set="benefits")


@register.simple_tag()
def get_slide_thumbnail(instance, size, method):
    image_file = None
    if instance and instance.image:
        image_file = instance.image
    return get_thumbnail(image_file, size, method, rendition_key_set="slides")
