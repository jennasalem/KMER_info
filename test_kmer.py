import pytest
import sys
from kmer_info import count_kmers, find_substrings, find_all_substrings, smallest_unique_k

def test_count_kmers():
    s = "ATGTCTGTCTGAA"
    k = 3
    assert count_kmers(s, k) == 7

def test_find_substrings():
    s = "ATGTCTGTCTGAA"
    k = 2
    expected = {"AT": {"TG"}, "TG": {"GA"}, "GT": {"TC"}, "TC": {"CT"}, "CT": {"TG"}, "GA": {"AA"}, "AA": {"A"}}
    assert find_substrings(s, k) == expected

def test_find_all_substrings():
    file_path = "test_sequences.txt"
    k = 2
    expected_output = {
        'seq1': {'AT': {'TG'}, 'TG': {'GA'}, 'GT': {'TC'}, 'TC': {'CT'}, 'CT': {'TG'}, 'GA': {'AA'}, 'AA': {'A'}},
        'sequence2': {'AG': {'GG'}, 'GG': {'GC'}, 'GC': {'CT'}, 'CT': {'TA'}, 'TA': {'AA'}, 'AC': {'CT'}, 'AA': {'A'}}
    }
    actual_output = find_all_substrings(file_path, k)
    assert find_all_substrings(file_path, k) == expected_output

def test_smallest_unique_k():
    file_path = "test_sequences.txt"
    assert smallest_unique_k(file_path) == 1

if __name__ == "__main__":
    sys.exit(pytest.main(sys.argv[1:]))
