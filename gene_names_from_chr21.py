"""
File   :  gene_names_from_chr21.py
This program takes gene symbol files in text format and converts the
assigned gene symbol and description columns into dictionary objects.
Finally, an infinite loop is applied using the user input as a key to
getting the stored values returning on the command line prompt. Once
the user inputs quit or exit, they can get just out of the loop.
Sample command for executing the program:
python3 gene_names_from_chr21.py -i chr21_genes.txt
"""

import sys
import argparse
from assignment4.io_utils import convert_cols_dict, get_filehandle


def get_cli_args():
    """
    CLI options using Python's argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(
        description="Open chr21_genes.txt, and ask user for a gene name")

    parser.add_argument('-i', '--infile', dest='infile',
                        type=str, help='Path to file to open', required=True)

    return parser.parse_args()


def main():
    """Main business logic"""
    args = get_cli_args()

    # Create a file read object from argparse infile
    fh_in = get_filehandle(args.infile, "r")

    # Convert the symbol and description to the dictionary, and pop out the title line.
    symbol_to_description = convert_cols_dict(fh_in, 0, 1)
    symbol_to_description.pop("Gene Symbol", None)

    # Listen to user input by while loop
    while True:
        input_symbol = input(
            "Enter gene name of interest. Typvhe quit to exit: ")
        # if the inputted symbol is in the dictionary, output its associated values
        if input_symbol in symbol_to_description:
            sys.stdout.write(symbol_to_description[input_symbol] + "\n")
        # if the inputted symbol is either quit or exit, output the message and break the loop
        elif input_symbol.lower() in ["quit", "exit"]:
            sys.stdout.write("Thanks for querying the data." + "\n")
            break
        # if the inputted symbol is not valid , output warning message
        else:
            sys.stdout.write("Not a valid gene name." + "\n")

    fh_in.close()


if __name__ == '__main__':
    main()
