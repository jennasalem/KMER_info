#!/usr/bin/env python3

#Starting example: Identifying all different observed substrings of size 2 in the example.

import sys 

s = "ATGTCTGTCTGAA" #define the genomic sequence you would like to use throughout the code

print(s[0:2]) # printing base 1-2 ... etc.
print(s[1:3])
print(s[2:4])
print(s[6:8])
print(s[8:10])
print(s[10:11])

print(s[0:2], s[2:4], s[4:6], s[6:8], s[8:10], s[10:11]) # printing all together with the kmer pattern

#Extending to identify all different observed substrings of any size, specified as k.

s = "ATGTCTGTCTGAA" # defining the sequence you want to use
k = 3  # or any other szie you would like to test

def count_kmers(s, k):
    """
    Counting the number of unique k-mers of size k in the given sequence s.

    Arguments:
    s (str): The input sequence.
    k (int): The size of the k-mers to count.

    Returns:
    int: The number of unique k-mers of size k in the input sequence.
    """
    kmers = set()
    for i in range(len(s) - k + 1):
        kmers.add(s[i:i+k]) # adding each kmer to the set
    return len(kmers) # returning the number of unique kmers

print(f"There are {count_kmers(s, k)} unique k-mers of the specified size {k}.") # output

#Extending to count the number of different observed substrings of all possible sizes.

s = "ATGTCTGTCTGAA"  # define sequence

def count_kmers_max(s, k_max):
    """
    Count the number of unique k-mers of sizes 1 to k_max in the given sequence s.

    Arguments:
    s (str): The input sequence.
    k_max (int): The maximum size of the k-mers to count.

    Returns:
    dict: A dictionary where the keys are the k-mer sizes and the values are the number of unique k-mers of each size in the input sequence.
    """
    kmers = {} # creating the dict where counts of unique kmers will be stored
    for k in range(1, k_max + 1):
        kmer_set = set()
        for i in range(len(s) - k + 1):
          kmer_set.add(s[i:i+k]) # adding each kmer to the set
          kmers[k] = len(kmer_set)
    return kmers

k_max = 3  # or any other value you want to test
print(count_kmers(s, k_max))


#FUNCTION 1
#Function to identify all substrings of size k for a single sequence, and all unique possible subsequent substrings

def find_substrings(s, k):
    """
    Find all substrings of size k in the given sequence s and their unique possible subsequent substrings.

    Arguments:
    s (str): The input sequence.
    k (int): The size of the substrings to find.

    Returns:
    dict: A dictionary where the keys are the substrings of size k and the values are the unique possible subsequent substrings of each substring.
    """
    substrings = {} # dictionary to store the substrings and their subsequent substrings
    for i in range(len(s) - k + 1):
        substring = s[i:i+k] # extracting the substrings of the size k
        subsequent_substrings = set() # list to store the unique possible subsequent substrings of each substring
        for j in range(i + 1, i + k): 
            subsequent_substrings.add(s[j:j+k]) # extract each unique possible subsequent substring of size j
        substrings[substring] = subsequent_substrings  # store the substrings and their subsequent substrings in the dictionary
    return substrings

s = "ATGTCTGTCTGAA"
k = 2  # or any other value you want to test
print(find_substrings(s, k))

#FUNCTION 2
#Function identifying all possible substrings and their subsequent substrings from a file.
def find_all_substrings(file_path, k):
    """
    Find all substrings of size k in the content of the given file and their unique possible subsequent substrings.

    Arguments:
    file_path (str): The path to the input file.
    k (int): The size of the substrings to find.

    Returns:
    dict: A dictionary where the keys are the substrings of size k and the values are the unique possible subsequent substrings of each substring.
    """
    substrings = {}  # dictionary to store the substrings and their subsequent substrings
    with open(file_path, 'r') as file:
        content = file.read()  # read content from file
        for i in range(len(content) - k + 1):
            substring = content[i:i+k]  # extracting the substrings of size k
            subsequent_substrings = set()  # set to store the unique possible subsequent substrings of each substring
            for j in range(i + 1, i + k):
                subsequent_substrings.add(content[j:j+k])  # extract each unique possible subsequent substring of size k
            substrings[substring] = subsequent_substrings  # store the substrings and their subsequent substrings in the dictionary
    return substrings

file_path = "../Python_439/reads.fa"  # specify the path to your file
k = 2  # or any other value you want to test
print(find_all_substrings(file_path, k))


#FUNCTION 3
#Function to find the smallest unique value using prior functions
def smallest_unique_k(file_path):
    """
    Find the smallest value of k such that every substring of length k in the given sequence has only one possible subsequent substring.

    Arguments:
    file_path (str): The path to the input file containing the sequence.

    Returns:
    int: The smallest value of k that satisfies the condition.
    """
    k = 1  # specify a k value, you can change this k value for a desired output
    while True:
        substrings = find_all_substrings(file_path, k) # find all substrings/subsequence substrings the length of k in the sequence
        unique_substrings = set()  # store all unique subsequent substrings
        for _, subsequent_substrings in substrings.items():
            unique_substrings.update(subsequent_substrings)
        if len(unique_substrings) == len(substrings) * (k - 1):
            return k
        k += 1
file_path = "../Python_439/reads.fa"  # specify the path to your file
k = smallest_unique_k(file_path)
print(f"The smallest value of k is {k}.") # prints the output

