#  Assignment4

## Description

Program Name: ***gene_names_from_chr21.py***
This program receives the user's input of the gene symbol
and, in return, its relevant description. If the information 
is invalid, it will throw the error message and ask for input
again. The program runs continuously until the user inputs
quit or exits, and the program stops.

Program Name: ***find_common_cats.py***
This program takes two files; one is the gene files and another 
is a gene category file as inputs to calculate the number of
the same category genes within the chr21_gene file. Finally,
it generates an output file called chr21_genes_categories.txt
that merges the category, occurrence, and descriptions columns
from both files into one. 

Program Name: ***intersection_of_gene_names.py***
This program finds the common gene symbol between two input files.
The output shows statistical results among two files, including
the two separate files' gene symbol length and the intersection's
standard gene length—finally, the file export text file of
intersected gene symbols in one column and analphabetic order.  


## Getting Started

* Hi, this is the documentation for assignment 4 of the bio programming course.
* This project demos students' capability in file handling, function testing, 
and statistic calculation using generic python code with a command line interface.
If you are interested in programming skills, this might be something for your 
reference.

### Dependencies

* Python version 3.8.10 and compatible modules (if needed) 

### Installing

* The file can download from the Canvas
* Python3 and Python IDE is required
* Required only use argparse,re,os,sys,and collections modules

### Executing program

* Use python IDE to open the file
* Run the python file by command line
* Follow exceptions if there is any error from command line input 
* Execute two programs are as followed

*** NO.1 gene_names_from_chr21.py ***
>>> python3 gene_names_from_chr21.py -i chr21_genes.txt

A successful output example is as follows: 
```
Enter gene name of interest. Type quit to exit:  TPTE

TPTE found! Here is the description: 
tensin, putative protein-tyrosine phosphatase, EC 3.1.3.48.

Enter gene name of interest. Type quit to exit: TPTTTT
Not a valid gene name.

Enter gene name of interest. Type quit to exit: qUiT
Thanks for querying the data.
```

*** NO.2 find_common_cats.py ***
>>> python3 find_common_cats.py -i1 chr21_genes.txt -i2 chr21_genes_categories.txt

A successful output file looks as follows and save as chr21_genes_categories.txt
in the OUTPUT directory.

```
   Category        Occurrence      Description
1.1     <Occurrence Here>     Genes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, 
```
No message on the command line since all the output goes to the file.


*** NO.3 intersection_of_gene_names.py ***
>>> python3 intersection_of_gene_names.py -i1 chr21_genes.txt -i2 HUGO_genes.txt

A statistical calculation result shows on the command line prompt.
```
Number of unique gene names in gene_age.txt: 307
Number of unique gene names in chr21_genes.txt: 285
Number of common gene symbols found: 4
Output stored in OUTPUT/intersection_output.txt

```

A successful output file will look as follows and will be save as
intersection_output.txt in the OUTPUT directory.

```
ABCG1
ADAMTS1
ADAMTS5
...
...
...
```

## Help

Any issue contact with yao.yao-@northeastern.edu

## Authors

Yao Chieh Yao
Northeastern University Bioinformatics

## Version History

* 1.0
    * Assignment01 Finish 
* 0.1
    * Assignment01 Release 

## License

This project is an assignment work and only license to TA and professors of Northeastern University Bioinformatics 

## Acknowledgments


