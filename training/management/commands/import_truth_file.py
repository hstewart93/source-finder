import csv

from django.core.management.base import BaseCommand

from training.models import TrueSource


class Command(BaseCommand):
    """Custom management command to read in a csv and create TrueSource objects
    in the database.

    Currently only supports .txt files."""

    help = "Reads in txt file and creates TrueSource objects in database from rows"

    def add_arguments(self, parser):
        """Add custom arguments to the management command"""
        parser.add_argument("filepath", nargs="+", type=str)
        parser.add_argument("header_end", nargs="+", type=int)

    def handle(self, *args, **options):
        """Method that reads in the file parsed as a command argument and creates
        TrueSource obejcts in the database from each row."""
        path = options["filepath"][0]
        if path.endswith(".txt"):
            with open(path, "r") as file:
                sources = file.readlines()

            for source in sources[options["header_end"][0] :]:
                features = source.split()
                model_fields = [
                    "source_id",
                    "ra_core",
                    "dec_core",
                    "ra_centroid",
                    "dec_centroid",
                    "flux",
                    "core_fraction",
                    "bmaj",
                    "bmin",
                    "position_angle",
                    "size",
                    "classification",
                    "selection",
                    "x_centroid",
                    "y_centroid",
                ]

                items = dict(zip(model_fields, features))
                TrueSource.objects.create(**items)
            print(f"Created {TrueSource.objects.all().count()} TrueSource objects")
