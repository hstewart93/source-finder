import pytest

from django.core.management import call_command

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


class TestImportTruthFile:
    """Tests for the import_truth_file management command."""

    def test_filepath_is_required(self):
        """"""
        pass

    def test_header_end_is_required(self):
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
