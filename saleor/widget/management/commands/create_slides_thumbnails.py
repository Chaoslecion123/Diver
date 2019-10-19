import logging

from django.core.management.base import BaseCommand
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from ...models import Slide

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate thumbnails for all slide images"

    def handle(self, *args, **options):
        self.warm_slide_images()

    def warm_slide_images(self):
        self.stdout.write("Slide image thumbnails generation:")
        warmer = VersatileImageFieldWarmer(
            instance_or_queryset=Slide.objects.all(),
            rendition_key_set="slides",
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
