import os

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

        # Add a required argument for file_path to be added to the command
        parser.add_argument("file_path", nargs="?", type=str)

        # Add an optional argument for row number where header ends to be added to the command
        parser.add_argument("header_end", nargs="?", type=int, default=17)

        # Add an optional argument to delete existing TrueSource data
        parser.add_argument(
            "--delete",
            action="store_true",
            dest="delete",
            help="Delete TrueSource objects.",
        )

    @staticmethod
    def create_objects(source):
        """Method to create TrueSource objects in the database given a source from
        the file lines read in."""
        items = dict(zip(MODEL_FIELDS, source.split()))
        return TrueSource.objects.create(**items)

    def handle(self, *args, **options):
        """Method that reads in the file parsed as a command argument and creates
        TrueSource obejcts in the database from each row."""
        if options["delete"]:
            TrueSource.objects.all().delete()
        if not options["file_path"]:
            raise Exception("No file path found, please enter a valid file path.")
        path = options["file_path"]
        if os.path.splitext(path)[-1] == ".txt":
            with open(path, "r") as file:
                lines = file.readlines()
            sources = lines[options["header_end"] + 1 :]
            pool = Pool(processes=cpu_count())
            pool.map(self.create_objects, sources)

            print(f"Created {TrueSource.objects.all().count()} TrueSource objects")

        else:
            raise Exception(
                "The file parsed is not of type .txt. This command currently only "
                "supports .txt files."
            )
