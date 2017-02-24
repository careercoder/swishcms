

from django.core.management.base import BaseCommand, CommandError
from django.utils import translation

class Command(BaseCommand):

    def handle(self, *args, **options):
        from swish.core.backend.components.installer.components import *
        SwishInstaller().get_components()