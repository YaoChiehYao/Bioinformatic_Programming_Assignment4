"""
File   :  intersection_of_gene_names.py
This program takes gene symbol files in text format, converts
the gene symbol column into set objects, and gets the intersected
genes. Finally, it calculates statistical output based on the
acquired data and writes it into output files.
Sample command for executing the program:
python3 intersection_of_gene_names.py -i1 chr21_genes.txt -i2 HUGO_genes.txt
"""

import argparse
from assignment4.io_utils import get_filehandle, convert_symbol_set, calculate_stats


def get_cli_args():
    """
    CLI options using Python's argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(
        description="Combine on gene name and count the category occurrence")

    parser.add_argument('-i1', '--infile1', dest='infile1',
                        type=str, help='Gene list 1 to open', required=True)
    parser.add_argument('-i2', '--infile2', dest='infile2',
                        type=str, help='Gene list 2 to open', required=True)

    return parser.parse_args()


def output_data(stats, intersection_output, gene_intersect):
    """Output file"""
    # Write gene intersection
    intersection_output.writelines('\n'.join(gene_intersect))
    # Write output message on cml
    print(f"""
    Number of unique gene names in hgnc_complete_set_reduced.txt: {stats.num_chr21}
    Number of unique gene names in HUGO_genes.txt: {stats.num_hugo}
    Number of common gene symbols found: {stats.num_common_gene}
    Output stored in {stats.outfile_path}
    """)


def main():
    """Main business logic"""
    # Make argparse object
    args = get_cli_args()

    # Create file handles
    chr21_genes = get_filehandle(args.infile1, "r")
    hugo_genes = get_filehandle(args.infile2, "r")
    outfile_path = "OUTPUT/intersection_output.txt"
    intersection_output = get_filehandle(outfile_path, "w")

    # Create gene symbol sets based on files
    chr21_gene_set = convert_symbol_set(chr21_genes)
    hugo_gene_set = convert_symbol_set(hugo_genes)

    # Make an intersection for two sets
    gene_intersect = sorted(chr21_gene_set.intersection(hugo_gene_set))

    # Calculate the statistical output
    output_stats = calculate_stats(
        chr21_gene_set, hugo_gene_set, gene_intersect, outfile_path)

    # Output instersected gene and stats
    output_data(output_stats, intersection_output, gene_intersect)
    chr21_genes.close()
    hugo_genes.close()


if __name__ == '__main__':
    main()
