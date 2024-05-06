# KMER_info
## A K-mer search for a genomic sequence
### Jenna Salem, University of Rhode Island, May 2024

# What is a k-mer?
A k-mer is simply a specific number of nucleotides/base-pairs within a DNA sequence. For example, a 3-mer (k-mer the size of 3) could be GCA from the sequence GCATGTCCCA. Essentially, all the k-mers within a sequence will overlap by 1:

GCA, CAT, ATG, TGT, GTC, TCC, CCC, CCA

K-mers are specifically important in the realm of bioinformatics, as defining them makes it easier to assemble genomes and also making analysis of smaller bits of sequence more manageable.

# About
KMER-info is a Python script created to find k-mers and subsequent k-mers from a specified genomic sequence. 
For more information about k-mers and what they are within the study of Bioinformatics:
  https://medium.com/swlh/bioinformatics-1-k-mer-counting-8c1283a07e29

# Installation
- In order to install and run this program, you need Python3 installed. 

- You also need to clone this GitHub repository
```
    git clone https://github.com/jennasalem/KMER_info
```

# Files
- assemble_genome.py is the main Python script that when run, outputs the subsequent k-mers
- test_assembly.py is the script used when testing the function

# How To Use KMER_info

# Input
The input for this code will be a genomic sequence of your choosing.
## Input Options
There are two input options for this program.
- Text of the genomic sequence, defined as s = "ATGTCTGTCTGAA". Using this input option is found in the beginning of the code.
- File that includes a genomic sequence, defined using file_path = ...

# Output
The output of each specific "question" varies. Listed below are explainations for each.

## Extending to identify all different observed substrings of any size, specified as k.
This is the first question posed within the code. This code will count the number of unique k-mers of a given size, specified as k. So, this code is highlighing the number of unique k-mers within the sequence. 
## Extending to count the number of different observed substrings of all possible sizes.

## Defining a function to identify all substrings of size k for a single sequence, and all unique possible subsequent substrings.

## Defining a function identifying all possible substrings and their subsequent substrings from a file.

## Defining a function to find the smallest unique value using prior functions.

# Usage: Example
Below is an example of how to use KMER_info, using python within your terminal.
Simply copy and paste the code, updating the sequence:

```
#Extending to identify all different observed substrings of any size, specified as k.
def count_kmers(s, k):
    """
    Count the number of unique k-mers of size k in the given sequence s.

    Arguments:
    s (str): The input sequence.
    k (int): The size of the k-mers to count.

    Returns:
    int: The number of unique k-mers of size k in the input sequence.
    """
    kmers = set()
    for i in range(len(s) - k + 1):
        kmers.add(s[i:i+k])
    return len(kmers)

s = "ATGTCTGTCTGAA" # defining the sequence you want to use throughout the code
k = 3  # or any other value you want to test
print(f"Number of unique k-mers of size {k}: {count_kmers(s, k)}")
```

or file path accordingly:

```
def find_all_substrings(file_path, k):
    """
    Find all substrings of size k in all sequences in the given file and their unique possible subsequent substrings.

    Arguments:
    file_path (str): The path to the input file containing the sequences.
    k (int): The size of the substrings to find.

    Returns:
    dict: A dictionary where the keys are the sequence names and the values are dictionaries containing the substrings of size k and their unique possible subsequent substrings.
    """
    substrings = {}
    with open(file_path, 'r') as file:
        sequence_name = None
        for line in file:
            if line.startswith(">"):
                if sequence_name:
                    print(f"Substrings for sequence {sequence_name}:")
                    print(substrings[sequence_name])
                sequence_name = line[1:].strip()
                substrings[sequence_name] = {}
            else:
                sequence = line.strip()
                substrings[sequence_name] = find_substrings(sequence, k)
    return substrings

file_path = "../Python_439/sequence.txt" # insert your file path here, make sure it is correct to ensure an output
k = 2  # or any other value you want to test
print(find_all_substrings(file_path, k))
```

# Testing using pytest
To test the code, there is a file within this repository named
