import pytest

from django.core.management import call_command

from training.models import TrueSource

# Create a pytest fixture that creates a text file
# can parse in content, some is valid content, some is invalid
# make VALID_CONTENT = ""
# make INVALID_CONTENT = ""
# can parse in file ending
# TEXT_FILE = ".txt", NOT_TEXT_FILE = ".csv"
# possibly add validation to the management command or just text the
# statement
# test parsing the wrong file type
# test not parsing a header_end value
# test not parsing a filepath value
# test no of objects created is expected from default content


@pytest.mark.django_db
class TestImportTruthFile:
    """Tests for the import_truth_file management command."""

    def test_filepath_is_required(self):
        """Test that the filepath argument is required to run the command."""
        with pytest.raises(Exception):
            call_command("import_truth_file")

    def test_delete_argument(self, text_file):
        """If the delete argument is parsed the object count will be the same as
        the number of lines in the input file as existing data will be deleted first."""
        call_command("import_truth_file", file_path=text_file, header_end=0)
        assert TrueSource.objects.all.count() == 10

    def test_header_end_default(self):
        """"""
        pass

    def test_exception_raised_for_invalid_file_type(self):
        """"""
        pass

    def test_invalid_content(self):
        """"""
        pass

    def test_object_created_count(self):
        """"""
        pass
