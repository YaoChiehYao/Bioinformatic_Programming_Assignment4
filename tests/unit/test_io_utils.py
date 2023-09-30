"""Test suite for io_utils.py"""
import os
import pytest

from assignment4.io_utils import (
    get_filehandle, merge_dict_value, convert_cols_dict, convert_symbol_set, calculate_stats)

FILE_TO_TEST = "test.txt"
TEXT1_FILE_TO_TEST = "test1.txt"
TEXT2_FILE_TO_TEST = "test2.txt"
TEXT_FILE_IMPORT_1 = """\
A2M	139	alpha-2-macroglobulin		5	21
ABL1	78	ABL proto-oncogene 1, non-receptor tyrosine kinase		5	69
"""

TEXT_FILE_IMPORT_2 = """\
A2M	139	alpha-2-macroglobulin		5	21
ATR	231	ATR serine/threonine kinase		7	49
"""


def test_existing_get_filehandle_for_reading():
    """Test get_filehandle for reading"""
    # does it open a file for reading
    # create a test file
    _create_file_for_testing(FILE_TO_TEST)
    # test
    test = get_filehandle(FILE_TO_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_TO_TEST)


def test_existing_get_filehandle_for_writing():
    """Test get_filehandle for writting"""
    # does it open a file for writing
    # test
    test = get_filehandle(file=FILE_TO_TEST, mode="w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_TO_TEST)


def test_get_filehandle_for_os_error():
    """Test get_filehandle for OSError"""
    # does it raise OSError
    # this should exit
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_for_value_error():
    """Test get_filehandle for ValueError"""
    # does it raise ValueError
    # this should exit
    _create_file_for_testing(FILE_TO_TEST)
    with pytest.raises(ValueError):
        get_filehandle("does_not_exist.txt", "rrr")
    os.remove(FILE_TO_TEST)


def _create_file_for_testing(file):
    """Test creat_file_for_testing for writting"""
    # not actually run, the are just helper funnctions for the test script
    # create a test file
    open(file, "w", encoding="utf-8").close()


def test_merge_dict_value():
    """Test merge_dict_value for merging two dictionary"""
    # merge two dictionaries by the common keys, and append values into a list
    assert merge_dict_value({'a': 1}, {'a': 2}) == {'a': [1, 2]}


def test_convert_cols_dict():
    """Test convert_cols_dict for converting cols to dictionary"""
    # convert two cols into dictionary
    _create_text_file_for_testing(TEXT1_FILE_TO_TEST, TEXT_FILE_IMPORT_1)
    test_dict = get_filehandle(TEXT1_FILE_TO_TEST, "r")
    output = convert_cols_dict(test_dict, 0, 1)
    assert output == {'A2M': '139', 'ABL1': '78'}
    assert isinstance(output, dict) is True
    os.remove(TEXT1_FILE_TO_TEST)


def test_convert_symbol_set():
    """Test convert_symbol_set for converting cols to set"""
    # convert one cols into set
    _create_text_file_for_testing(TEXT1_FILE_TO_TEST, TEXT_FILE_IMPORT_1)
    test_set = get_filehandle(TEXT1_FILE_TO_TEST, "r")
    output = convert_symbol_set(test_set)
    assert output == {"A2M", "ABL1"}
    assert isinstance(output, set) is True
    os.remove(TEXT1_FILE_TO_TEST)


def test_calculate_stats():
    """Test calculate_stats for calculating statistic"""
    # calculate statistic, and store results in collections
    _create_text_file_for_testing(TEXT1_FILE_TO_TEST, TEXT_FILE_IMPORT_1)
    _create_text_file_for_testing(TEXT2_FILE_TO_TEST, TEXT_FILE_IMPORT_2)
    test_set_1 = get_filehandle(TEXT1_FILE_TO_TEST, "r")
    test_set_2 = get_filehandle(TEXT2_FILE_TO_TEST, "r")
    set_1 = convert_symbol_set(test_set_1)
    set_2 = convert_symbol_set(test_set_2)
    set_intersect = set_1.intersection(set_2)
    assert len(set_1) == 2
    assert len(set_2) == 2
    assert len(set_intersect) == 1
    assert calculate_stats(set_1, set_2, set_intersect,
                           "output/test.txt") == (2, 2, 1, "output/test.txt")
    os.remove(TEXT1_FILE_TO_TEST)
    os.remove(TEXT2_FILE_TO_TEST)


def _create_text_file_for_testing(output_name, text_file):
    """Test create_text_file+for_testing for creating file object"""
    # not actually run, the are just helper funnctions for the test script
    # create text files for testing dict and set conversion
    file_handle = get_filehandle(output_name, "w")
    file_handle.write(text_file)
    file_handle.close()
