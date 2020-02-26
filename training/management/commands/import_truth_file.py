from django.core.management.base import BaseCommand
from multiprocessing import cpu_count, Pool

from training.models import TrueSource


MODEL_FIELDS = [
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


class Command(BaseCommand):
    """Custom management command to read in a csv and create TrueSource objects
    in the database.

    Currently only supports .txt files."""

    help = "Reads in txt file and creates TrueSource objects in database from rows"

    def add_arguments(self, parser):
        """Add custom arguments to the management command"""
        parser.add_argument("filepath", nargs="+", type=str)
        parser.add_argument("header_end", nargs="+", type=int)

    @staticmethod
    def create_objects(source):
        """Method to create TrueSource objects in the database given a source from
        the file lines read in."""
        items = dict(zip(MODEL_FIELDS, source.split()))
        return TrueSource.objects.create(**items)

    def handle(self, *args, **options):
        """Method that reads in the file parsed as a command argument and creates
        TrueSource obejcts in the database from each row."""
        path = options["filepath"][0]
        if path.endswith(".txt"):
            with open(path, "r") as file:
                lines = file.readlines()
            sources = lines[options["header_end"][0] :]

            pool = Pool(processes=cpu_count())
            pool.map(self.create_objects, sources)

            print(f"Created {TrueSource.objects.all().count()} TrueSource objects")

        else:
            raise Exception(
                "The file parsed is not of type .txt. This command currently only "
                "supports .txt files."
            )
