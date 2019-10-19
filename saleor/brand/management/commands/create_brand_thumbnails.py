import logging

from django.core.management.base import BaseCommand
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from ...models import Brand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate thumbnails for all brand images"

    def handle(self, *args, **options):
        self.warm_brand_logos()

    def warm_brand_logos(self):
        self.stdout.write("Brand logo thumbnails generation:")
        warmer = VersatileImageFieldWarmer(
            instance_or_queryset=Brand.objects.exclude(image=""),
            rendition_key_set="brands",
            image_attr="image",
            verbose=True,
        )
        _, failed_to_create = warmer.warm()
        self.log_failed_images(failed_to_create)

    def log_failed_images(self, failed_to_create):
        if failed_to_create:
            self.stderr.write("Failed to generate thumbnails:")
            for patch in failed_to_create:
                self.stderr.write(patch)
