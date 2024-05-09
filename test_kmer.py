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
    file_path = "reads.fa"
    k = 2
    expected = {"GA": {"AT"}, "AA": {"AC"}, "AT": {"TA"}, "TT": {"TA"}, "TC": {"CA"}}
    expected_first_5 = {key: expected[key] for key in list(expected.keys())[:5]}
    actual = find_all_substrings(file_path, k)
    actual_first_5 = {key: actual[key] for key in list(actual.keys())[:5]}
    expected_sorted = {key: sorted(value) for key, value in expected_first_5.items()}
    actual_sorted = {key: sorted(value) for key, value in actual_first_5.items()}
    
    assert actual_sorted == expected_sorted


def test_smallest_unique_k():
    file_path = "reads.fa"
    assert smallest_unique_k(file_path) == 1

if __name__ == "__main__":
    sys.exit(pytest.main(sys.argv[1:]))
