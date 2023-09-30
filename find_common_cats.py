"""
File   :  find_common_cats.py
This program takes gene symbol files in text format and converts the
assigned columns to dictionary objects. Finally, the dictionaries
merged by their standard keys into a merged dictionary and are used
to write a table to output files.
Sample command for executing the program:
python3 find_common_cats.py -i1 chr21_genes.txt -i2 chr21_genes_categories.txt
"""

import argparse
from collections import Counter
from assignment4.io_utils import get_filehandle, convert_cols_dict, merge_dict_value


def get_cli_args():
    """
    CLI options using Python's argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(
        description="Combine on gene name and count the category occurrence")

    parser.add_argument('-i1', '--infile1', dest='infile1',
                        type=str, help='Path to the gene description', required=True)
    parser.add_argument('-i2', '--infile2', dest='infile2',
                        type=str, help='Path to the gene category to open', required=True)
    return parser.parse_args()


def output_data(merge_dict, file_out):
    """Output file"""
    # Write column header
    file_out.writelines(
        "\t".join(("Gene_Symbol", "Occurrence", "Discription" + "\n")))
    # Write column body
    for key, value in merge_dict.items():
        file_out.writelines("\t".join((key, str(value[0]), value[1] + "\n")))


def main():
    """Main business logic"""
    # Make argparse object
    args = get_cli_args()

    # Create file handles
    chr21_gene_description = get_filehandle(args.infile1, "r")
    chr21_gene_category = get_filehandle(args.infile2, "r")
    categories = get_filehandle("OUTPUT/categories.txt", "w")

    # Get the gene symbol and description columns to dictionary
    symbol_counts = convert_cols_dict(chr21_gene_description, 0, 2)
    # Pop the column title and count duplicates of the category
    symbol_counts.pop("Gene Symbol", None)
    occurrence = Counter(symbol_counts.values())

    # Get the gene symbol and category columns to the dictionary
    discription = convert_cols_dict(chr21_gene_category, 0, 1)

    # Merge two dictionaries and output data
    dict_merged = merge_dict_value(occurrence, discription)

    # Pop one empty key-value pair out
    dict_merged.pop('', None)

    output_data(dict(sorted(dict_merged.items())), categories)
    chr21_gene_description.close()
    chr21_gene_category.close()


if __name__ == '__main__':
    main()
