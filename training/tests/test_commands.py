import pytest

from django.core.management import call_command

from training.models import TrueSource


@pytest.mark.django_db
class TestImportTruthFile:
    """Tests for the import_truth_file management command."""

    def test_filepath_is_required(self):
        """Test that the filepath argument is required to run the command."""
        with pytest.raises(Exception):
            call_command("import_truth_file")

    def test_create_objects_no_delete(self, valid_text_file):
        """The expected number of objects are created when the command is called
        without the delete argument."""
        original_count = TrueSource.objects.all().count()
        call_command("import_truth_file", file_path=valid_text_file, header_end=0)
        assert TrueSource.objects.all().count() == original_count + 20

    def test_create_objects_with_delete(self, valid_text_file):
        """If the delete argument is parsed the object count will be the same as
        the number of lines in the input file as existing data will be deleted first."""
        original_count = TrueSource.objects.all().count()
        call_command("import_truth_file", file_path=valid_text_file, header_end=0)
        new_count = TrueSource.objects.all().count()
        assert new_count == original_count + 20

        # Call command again without delete argument
        call_command("import_truth_file", file_path=valid_text_file, header_end=0)
        next_count = TrueSource.objects.all().count()
        assert next_count == new_count + 20

        # Call command with delete argument
        call_command(
            "import_truth_file", file_path=valid_text_file, header_end=0, delete=1
        )
        final_count = TrueSource.objects.all().count()
        assert final_count == 20
        assert final_count < next_count

    def test_header_end_default(self, valid_text_file):
        """If no header_end argument parsed the default is 17."""
        count = TrueSource.objects.all().count()
        call_command("import_truth_file", file_path=valid_text_file)
        assert TrueSource.objects.all().count() == count + 3

    def test_exception_raised_for_invalid_file_type(self, valid_csv_file):
        """If a file type that isn't a text file is parsed as an argument an
        Exception is raised."""
        with pytest.raises(Exception):
            call_command("import_truth_file", file_path=valid_csv_file)

    def test_invalid_content(self):
        """"""
        # TODO: write method to test validity of content
        pass
