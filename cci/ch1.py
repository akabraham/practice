from copy import deepcopy


# 1.1
def is_all_unique(s):
    return sorted(set(s)) == sorted(s)


# 1.1
def is_all_unique_no_special(s):
    """
    Returns whether a string has all unique characters, without use of
    additional data structures. Assumes at least 1 character.
    """
    ordered = sorted(s)
    for i, letter in enumerate(ordered):
        if i + 1 == len(ordered):
            break
        if letter == ordered[i+1]:
            return False

    return True


# 1.2
def special_reverse(s):
    """Reverse a string without using `reverse` or anything fancy."""
    length = len(s)
    lst = [s[length - 1 - i] for i, letter in enumerate(s)]
    return ''.join(lst)


# 1.3
def is_permutation(a, b):
    """Returns whether a is a permutation of b"""
    return sorted(a) == sorted(b)


# 1.4
def replace_spaces(s):
    return s.replace(' ', '%20')


# 1.5
def compress_strings(s):
    """
    Returns compressed strings. If original string is shorter than the
    compressed string, return the original.
    e.g. 'aabcccccaaa' ==> 'a2b1c5a3'
    """
    cnt = 1
    compressed = []
    for i, letter in enumerate(s):
        if i < len(s) - 1 and letter == s[i+1]:
            cnt += 1
        else:
            compressed.append('{}{}'.format(letter, cnt))
            cnt = 1

    if len(compressed) >= len(s):
        return s

    return ''.join(compressed)


# 1.6
def rotate_matrix(m):
    """Rotates an nxn matrix 90 degrees"""
    return [list(tup) for tup in zip(*reversed(m))]


# 1.7
def zeroify_matrix(m):
    """
    In an mxn matrix, if an element is 0, replaces its row and column with all
    0's
    """
    m1 = deepcopy(m)
    cols = set()

    for i, row in enumerate(m):
        for j, elem in enumerate(row):
            if j in cols:
                m1[i][j] = 0

            if elem == 0:
                cols.add(j)
                m1[i] = [0] * len(row)

    return m1


# 1.8
def _is_substring(a, b):
    """Returns whether a is a substring of b"""
    return a in b


# 1.8
def is_string_rotation(a, b):
    """
    Returns whether a is a rotation of b.
    e.g. 'waterbottle' is a rotation of 'erbottlewat'
    """
    if sorted(a) != sorted(b):
        return False

    return _is_substring(a, b * 2)


if __name__ == '__main__':
    assert special_reverse('theology') == 'ygoloeht'
    assert special_reverse('eye') == 'eye'
    assert special_reverse('g') == 'g'

    assert is_permutation('hater', 'earth') is True
    assert is_permutation('haters', 'earth') is False
    assert is_permutation('eggs', 'eggs') is True

    assert replace_spaces('Mr John Smith') == 'Mr%20John%20Smith'
    assert replace_spaces('Star Wars') == 'Star%20Wars'
    assert replace_spaces('google') == 'google'

    assert compress_strings('aabcccccaaa') == 'a2b1c5a3'
    assert compress_strings('shining') == 'shining'

    m1 = [['a', 'b'],
          ['c', 'd']]
    m2 = [['a', 'b', 'c'],
          ['d', 'e', 'f'],
          ['g', 'h', 'i']]
    assert rotate_matrix(m1) == [['c', 'a'],
                                 ['d', 'b']]
    assert rotate_matrix(m2) == [['g', 'd', 'a'],
                                 ['h', 'e', 'b'],
                                 ['i', 'f', 'c']]
    m3 = [[0, 4, 1],
          [7, 9, 2]]
    assert zeroify_matrix(m3) == [[0, 0, 0],
                                  [0, 9, 2]]
    m4 = [['a', 0, 'c'],
          ['d', 'e', 'f'],
          ['g', 'h', 'i']]
    assert zeroify_matrix(m4) == [[0, 0, 0],
                                  ['d', 0, 'f'],
                                  ['g', 0, 'i']]
    assert _is_substring('ten', 'tenth') is True
    assert _is_substring('tech', 'trench') is False

    assert is_string_rotation('waterbottle', 'erbottlewat') is True
    assert is_string_rotation('makeshift', 'shimakeft') is False
    assert is_string_rotation('watermelon', 'meloncholywater') is False

    print('all good')
