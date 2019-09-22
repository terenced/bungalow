import csv
import os

from django.db import transaction

from api.core.models import Listing, Metadata, SalesHistory
from api.core.utils.parse_date import parse_date
from api.core.utils.parse_price import parse_price
from api.core.utils.parse_numbers import parse_int, parse_float
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Import data from CSV (Only Zillow is supported)"

    def add_arguments(self, parser):
        parser.add_argument("filename", type=str)
        parser.add_argument(
            '--peak',
            action='store_true',
            help='Prints then 1st 10 lines',
        )

    def handle(self, *args, **options):
        filename = options["filename"]

        if not os.path.exists(filename):
            raise CommandError(f"'{filename}' does not exist")

        with open(filename, 'r') as file: 
            reader = csv.DictReader(file)
            for i, row in enumerate(reader):
                if options["peak"]:
                    self.stdout.write(', '.join(row))
                    if i >= 10:
                        break
                else:
                    self.save_data(row)

        self.stdout.write(self.style.SUCCESS("All Done!"))

    def save_data(self, row):
        try:
            with transaction.atomic():
                listing = Listing(
                    address=row['address'],
                    area_unit=row['area_unit'],
                    bathrooms=parse_float(row['bathrooms']),
                    bedrooms=row['bedrooms'],
                    city=row['city'],
                    home_size=parse_int(row['home_size']),
                    home_type=row['home_type'],
                    price=parse_price(row['price']),
                    property_size=parse_int(row['property_size']),
                    state=row['state'],
                    year_built=parse_int(row['year_built']),
                    zipcode=row['zipcode'],
                )
                listing.save()

                metadata = Metadata(
                    listing=listing,
                    source="zillow",
                    external_id=row["zillow_id"],
                    external_link=row["link"],
                )
                metadata.save()
                
                if row['last_sold_date'] and row['last_sold_price']:
                    sale_history = SalesHistory(
                        listing=listing,
                        sold_date=parse_date(row['last_sold_date']),
                        sold_price=parse_price(row['last_sold_price']),
                    )
                    sale_history.save()
                self.stdout.write(f"Created {listing}")
        except Exception as e:
            self.stdout.write("Skipping row due to error", row, e)
