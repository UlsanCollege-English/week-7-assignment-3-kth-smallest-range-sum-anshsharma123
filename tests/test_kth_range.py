import os, sys
import pytest

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from kth_range import Node, insert, kth_smallest, range_sum_bst

def build(vals):
    r = None
    for v in vals:
        r = insert(r, v)
    return r

# normal (4)
def test_kth_smallest_basic():
    r = build([5,3,7,2,4,6,8])
    assert kth_smallest(r, 1) == 2
    assert kth_smallest(r, 4) == 5

def test_range_sum_basic():
    r = build([10,5,15,3,7,18])
    assert range_sum_bst(r, 7, 15) == 32  # 7 + 10 + 15

def test_insert_reject_dups():
    r = build([2,1,3,3])
    # Tree should be 1, 2, 3
    assert kth_smallest(r, 1) == 1
    assert kth_smallest(r, 2) == 2
    assert kth_smallest(r, 3) == 3
    # Test that k=4 raises an error because '3' was rejected
    with pytest.raises(IndexError):
        kth_smallest(r, 4)

def test_kth_last():
    r = build([5,1,9,0,3,7,10])
    # Tree: 0, 1, 3, 5, 7, 9, 10
    assert kth_smallest(r, 7) == 10

# edge (3)
def test_empty_tree_range():
    assert range_sum_bst(None, 0, 100) == 0

def test_k_too_large():
    r = build([1,2,3])
    with pytest.raises(IndexError):
        kth_smallest(r, 5)

def test_single_node():
    r = build([42])
    assert kth_smallest(r, 1) == 42
    assert range_sum_bst(r, 0, 100) == 42

# harder (3)
def test_unbalanced_tree():
    r = build([1,2,3,4,5,6,7,8])
    assert kth_smallest(r, 6) == 6

def test_range_no_overlap():
    r = build([10,5,15,3,7,18])
    assert range_sum_bst(r, -10, -1) == 0
    assert range_sum_bst(r, 100, 200) == 0

def test_range_partial_edges():
    r = build([10,5,15,3,7,18])
    assert range_sum_bst(r, 5, 7) == 12 # 5 + 7