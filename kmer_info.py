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
    Finding all substrings of length k in the given sequence.

    Arguments:
    s (str): The input sequence.
    k (int): The length of the substrings to find.

    Returns:
    dict: A dictionary containing each substring of length k and its possible subsequent substrings.
    """
    substrings = {} # creating dictionary to store the substring and possible subsequent substrings
    with open(file_path, 'r') as file:
        sequence_name = None # no sequence defined, as we are using a file path for this code
        for line in file: # iterating over all possible substrings of length, k
            if line.startswith(">"): # if line starts with '>', indicates new sequence. This can be used if your file has more than one sequence
                if sequence_name:
                    substrings[sequence_name] = find_substrings(sequence, k)  # finding substrings and their subsequent substrings for the sequence
                sequence_name = line[1:].strip()  # extracting sequence name from the line
                substrings[sequence_name] = {}  # new entry in the dictionary for sequence
            else:  # if the line does not start with '>', it contains the sequence data (if file only contains one sequence)
                sequence = line.strip()  # extracting the data
    if sequence_name:
        substrings[sequence_name] = find_substrings(sequence, k)  # find the substrings and their subsequent substrings for the last sequence in the file
    return substrings

file_path = "../../shared/439539/reads.fa" # insert your file path here, make sure it is correct to ensure an output
k = 2  # or specify any other value you want to test
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
    with open(file_path, 'r') as file: # reading sequence within the file
        s = file.read().strip()
    k = 1 # specify a k value, you can change this k value for a desired output
    while True:
        substrings = find_substrings(s, k) # find all substrings/subsequence substrings the length of k in the sequence
        unique_substrings = set() # empty set to store the unique substrings
        for substring in substrings:
            for subsequent_substring in substrings[substring]: # iterating all possible subsequent substrings for the current substring
                key = substring + subsequent_substring # key to chain the current substring and subsequent substring
                if key not in unique_substrings: # if key has not been seen before, it is added to set of unique substrings
                    unique_substrings.add(key)
                else:
                    break # if key has been seen before, break out of loop and continue onto the next substring
            else:
                return k # if there are subsequent substrings that have been seen before, return the value of k
        k += 1 # increment value of k
file_path = "../../shared/439539/reads.fa" # input file path
k = smallest_unique_k(file_path) 
print(f"The smallest value of k is {k}.") # prints the output
