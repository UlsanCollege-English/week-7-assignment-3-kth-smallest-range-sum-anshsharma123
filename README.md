[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/GUbefOLC)

# Kth Smallest & Range Sum (BST)

## Story
A product index stores prices as integers in a BST. You need:
1) the **kth smallest** price, and  
2) the **sum** of prices in a given inclusive range `[low, high]`.

## Task (What to Build)
In `src/kth_range.py`:
- `insert(root, key) -> Node`: insert key with duplicate-reject; return (possibly new) root.
- `kth_smallest(root, k) -> int`: 1-based kth smallest.
- `range_sum_bst(root, low, high) -> int`: sum of keys in range.

## Hints
- Inorder traversal yields sorted order; count nodes until you reach `k`.
- For range sum, **prune**:  
  - if `node.key < low`, skip left;  
  - if `node.key > high`, skip right.
- Raise an error for `k` larger than the number of nodes.

## Run Tests Locally
```bash
python -m pytest -q
```

## Common Problems

- Off-by-one on k (remember 1-based).
- Traversing into subtrees that can’t contain valid values (missed pruning).
- Not guarding None checks.

## Complexity
- insert: O(h) time.
- kth_smallest: O(h + k) time, O(h) space (stack).
- range_sum_bst: O(h + m) where m is number of in-range nodes; O(h) space.

## Example
```bash
Tree: [5,3,7,2,4,6,8]
kth_smallest(root, 4) == 5
range_sum_bst(root, 7, 15) == 7 + 8 = 15 (if those are the only in-range nodes)
```