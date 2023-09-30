"""
File   :  io_utils.py
This program covers the used modules in the assignment4
programs, gene_names_from_chr21.py , find_common_cats.py
and intersection_of_gene_names.py. Those modules are imported
to the test file and tested by pytest. Finally, we can see the
total test result on the coverage file.
"""

import sys
from collections import namedtuple, defaultdict


def get_filehandle(file=None, mode=None):
    """
    filehandle : get_filehandle(infile, "r")
    Takes : 2 arguments file name and mode i.e. what is needed to be done with
    this file. This function opens the file based on the mode passed in
    the argument and returns filehandle.
    @param file: The file to open for the mode
    @param mode: They way to open the file, e.g. reading, writing, etc
    @return: filehandle
    """

    try:
        fobj = open(file, mode, encoding="utf-8")
        return fobj
    except OSError:
        print(
            f"Could not open the file: {file} for type '{mode}'", file=sys.stderr)
        raise
    except ValueError:
        print(
            f"Could not open the file: {file} for type '{mode}'", file=sys.stderr)
        raise


def merge_dict_value(dict_1, dict_2):
    """Merge two dictionaries by the same keys """
    # Use defaultdict to get two dictionary values into a list
    merge_dict = defaultdict(list)
    for info in (dict_1, dict_2):
        for key, value in info.items():
            merge_dict[key].append(value)
    return merge_dict


def convert_cols_dict(fh_in, first_col=None, second_col=None):
    """Parse txt file to dictionary """
    data = {}
    # Split by delimiter and extract 1st and 2nd col to dict
    for line in fh_in:
        data[line.split("\t")[first_col].rstrip()
             ] = line.split("\t")[second_col].rstrip()
    return data


def convert_symbol_set(text_file):
    """Parse txt file to set """
    # Split by delimiter and extract 1st col to set
    split_file = set()
    for data in text_file:
        split_file.add(data.split()[0])
    return split_file


def calculate_stats(set_1, set_2, set_intersect, outfile_path):
    """Calculate the output statistic """
    # Use collections to get the statistical results
    stats = namedtuple(
        "statistics", "num_chr21 num_hugo num_common_gene outfile_path")
    output_stats = stats(len(set_1), len(
        set_2), len(set_intersect), outfile_path)
    return output_stats
