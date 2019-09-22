from api.core.models import Listing, Metadata, SalesHistory
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Empties the Database"

    def handle(self, *args, **options):
        Listing.objects.all().delete()
