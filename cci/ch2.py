from operator import itemgetter


# 2.1
def remove_duplicates(l):
    """Remove duplicates from a list"""
    seen = set()
    for i, elem in enumerate(l):
        if elem in seen:
            l.pop(i)
        else:
            seen.add(elem)

    return l


# 2.1
def remove_duplicates_no_buffer(l):
    """Removes duplicates from a list without using a buffer"""
    d = {}
    for i, elem in enumerate(l):
        if elem not in d:
            d[elem] = i

    return [k for k, v in sorted(d.items(), key=itemgetter(1))]


# NOTE: if you need to use sorted, the object to sort must be an iterable.
# That means to sort a dict `d`, you'll need `d.items()`.


# 2.2
def find_kth_to_last(l, k):
    """Finds the kth to last element in a list"""
    return l[-k]


# 2.3
def remove_middle(l, node):
    """Remove a node from the middle of list"""
    if len(l) % 2 == 0:  # two middles
        middle_lower_idx = (len(l) - 1) // 2
        middle_upper_idx = middle_lower_idx + 1
        for idx in (middle_lower_idx, middle_upper_idx):
            if l[idx] == node:
                l.pop(idx)
                break
    else:  # single middle
        middle_idx = (len(l) - 1) // 2
        if l[middle_idx] == node:
            l.pop(middle_idx)


# 2.4
def partition_list(l, x):
    """
    Partition list around value x, such that all nodes less than x come before
    all nodes greater than or equal to x
    """
    return sorted(l)


# 2.5
def sum_special_lists(a, b):
    """
    Returns the sum of two lists, where each list represents a number in reverse
    order.
    e.g. [7, 1, 6] + [5, 9, 2] = [2, 1, 9] (that is, 617 + 295 = 912)
    """
    def _encode_to_list(n):
        return [int(x) for x in reversed(str(n))]

    def _decode_to_number(l):
        return int(''.join(str(x) for x in reversed(l)))

    sum_number = _decode_to_number(a) + _decode_to_number(b)
    return _encode_to_list(sum_number)


# 2.5_pt2
def sum_special_lists_forward(a, b):
    """
    Returns the sum of two lists, where each list represents a number in
    ascending order.
    e.g. [6, 1, 7] + [2, 9, 5] = [9, 1, 2] (that is, 617 + 295 = 912)
    """
    def _encode_to_list(n):
        return [int(x) for x in str(n)]

    def _decode_to_number(l):
        return int(''.join(str(x) for x in l))

    sum_number = _decode_to_number(a) + _decode_to_number(b)
    return _encode_to_list(sum_number)


# 2.6
def beginning_of_circular_list(l):
    """Returns the beginning of a circular list. Assumes items are unique."""
    seen = set()
    for elem in l:
        if elem in seen:
            return elem
        else:
            seen.add(elem)
    else:
        return None


# 2.7
def is_palindrome(l):
    """Returns whether a list is a palindrome"""
    return l == l[::-1]


if __name__ == '__main__':
    l1 = ['a', 'b', 'b', 'c']
    l2 = ['d', 'e']
    l3 = [0, 0, 4]
    l4 = ['the', 'cat', 'jumped', 'over', 'the', 'lazy', 'dog']
    l5 = ['a', 'b', 'b', 'a', 'c', 'd']

    assert remove_duplicates(l1) == ['a', 'b', 'c']
    assert remove_duplicates(l2) == l2
    assert remove_duplicates(l3) == [0, 4]
    assert remove_duplicates(l4) == [
        'the', 'cat', 'jumped', 'over', 'lazy', 'dog']

    l1 = ['a', 'b', 'b', 'c']
    l2 = ['d', 'e']
    l3 = [0, 0, 4]
    l4 = ['the', 'cat', 'jumped', 'over', 'the', 'lazy', 'dog']
    l5 = ['a', 'b', 'b', 'a', 'c', 'd']

    assert remove_duplicates_no_buffer(l1) == ['a', 'b', 'c']
    assert remove_duplicates_no_buffer(l2) == l2
    assert remove_duplicates_no_buffer(l3) == [0, 4]
    assert remove_duplicates_no_buffer(l4) == [
        'the', 'cat', 'jumped', 'over', 'lazy', 'dog']

    assert find_kth_to_last(l1, 2) == 'b'
    assert find_kth_to_last(l1, 1) == 'c'
    assert find_kth_to_last(l2, 2) == 'd'
    assert find_kth_to_last(l3, 1) == 4
    assert find_kth_to_last(l4, 5) == 'jumped'
    assert find_kth_to_last(l5, 2) == 'c'

    l1 = ['a', 'b', 'b', 'c']
    l2 = ['d', 'e']
    l3 = [0, 0, 4]
    l4 = ['the', 'cat', 'jumped', 'over', 'the', 'lazy', 'dog']
    l5 = ['a', 'b', 'b', 'a', 'c', 'd']

    remove_middle(l1, 'b')
    assert l1 == ['a', 'b', 'c']
    remove_middle(l2, 'd')
    assert l2 == ['e']
    remove_middle(l3, 0)
    assert l3 == [0, 4]
    remove_middle(l4, 'over')
    assert l4 == ['the', 'cat', 'jumped', 'the', 'lazy', 'dog']
    remove_middle(l5, 'a')
    assert l5 == ['a', 'b', 'b', 'c', 'd']

    l1 = ['a', 'b', 'b', 'c']
    l2 = ['d', 'e']
    l3 = [0, 0, 4]
    l4 = ['the', 'cat', 'jumped', 'over', 'the', 'lazy', 'dog']
    l5 = ['a', 'b', 'b', 'a', 'c', 'd']
    l6 = ['g', 'x', 'q', 'h']
    l7 = ['d', 'e', 'c']
    l8 = [0, 10, 4]

    assert partition_list(l1, 'c') == ['a', 'b', 'b', 'c']
    assert partition_list(l4, 'cat') == [
        'cat', 'dog', 'jumped', 'lazy', 'over', 'the', 'the']
    assert partition_list(l5, 'c') == ['a', 'a', 'b', 'b', 'c', 'd']
    assert partition_list(l6, 'x') == ['g', 'h', 'q', 'x']
    assert partition_list(l7, 'd') == partition_list(l7, 'e') == \
        partition_list(l7, 'c') == ['c', 'd', 'e']
    assert partition_list(l8, 4) == [0, 4, 10]

    assert sum_special_lists([7, 1, 6], [5, 9, 2]) == [2, 1, 9]
    assert sum_special_lists_forward([6, 1, 7], [2, 9, 5]) == [9, 1, 2]

    assert beginning_of_circular_list([1, 6, 2, 6]) == 6
    assert beginning_of_circular_list(['a', 'c', 'e', 'b', 'x', 'a']) == 'a'

    assert is_palindrome(['a', 'b', 'b', 'a']) is True
    assert is_palindrome(['b', 'k', 'b']) is True
    assert is_palindrome(['a', 'a', 'a']) is True
    assert is_palindrome(['c', 'd', 'd', 'g']) is False

    print('all passed')
