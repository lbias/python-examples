import collections
import itertools
import sys
import timeit
import unittest

from typing import Callable, Iterable, Tuple


def oddity(iterable: Iterable,
           key: Callable[[object], object]=None,
           first: bool=False) -> Tuple[object, object]:
    """Find the element that is different.

    Args:
        iterable:
            Any iterable. Can be an infinite sequence *if* ``first`` is
            specified *and* there is a common item *and* at least one
            different item.
        key:
            A function used to extract a comparison key from each
            element; if not provided, the elements themselves are
            compared.
        first:
            Return early when the first uncommon item is found. This can
            be *much* faster when the uncommon item is near the front of
            the iterable, but it also adds a bit of overhead. The items
            won't be validated when using this, but it will work with
            infinite sequences.

    Returns:
        object:
            The key of the common element
        object:
            The different element or ``None`` if all the elements are
            equal.

    Raises:
        EmptyError:
            The sequence is empty.
        TooManyDistinctValuesError:
            2 or more distinct elements are found (determined by their
            keys). The string ``'123'`` will trigger this error.
        TooManyCommonValuesError:
            Multiple common elements are found. The string ``'11222``
            will trigger this error.
        NoCommonValueError:
            No common element is found. The string ``'12'`` will trigger
            this error.

    """
    seen = []
    common = []
    uncommon = []

    for item in iter(iterable):
        item_key = key(item) if key else item

        if item_key in seen:
            if item_key in common:
                if first and uncommon:
                    return item_key, uncommon[1]
            else:
                common.append(item_key)
                if len(common) == 2:
                    raise TooManyCommonValuesError

                if item_key in uncommon:
                    i = uncommon.index(item_key)
                    j = i + 2
                    uncommon[i:j] = []
        else:
            seen.append(item_key)
            if len(seen) == 3:
                raise TooManyDistinctValuesError
            uncommon.extend((item_key, item))

    if len(seen) == 0:
        raise EmptyError

    if len(common) == 0:
        raise NoCommonValueError

    if len(uncommon) == 0:
        # All values are the same
        uncommon_value = None
    else:
        uncommon_value = uncommon[1]

    return common[0], uncommon_value


def oddity_groupby(items, key=None, _sentinel=object()):
    sorted_items = sorted(items, key=key)
    grouped_items = itertools.groupby(sorted_items, key=key)

    a_key, a_group = next(grouped_items, (None, None))

    if a_group is None:
        raise EmptyError

    a1 = next(a_group, _sentinel)
    a2 = next(a_group, _sentinel)

    b_key, b_group = next(grouped_items, (None, None))

    if b_group is None:
        return a_key, None

    b1 = next(b_group, _sentinel)
    b2 = next(b_group, _sentinel)

    c = next(grouped_items, None)

    if c is not None:
        raise TooManyDistinctValuesError

    if a2 is _sentinel:
        if b2 is _sentinel:
            raise NoCommonValueError
        return b_key, a1

    if b2 is _sentinel:
        if a2 is _sentinel:
            raise NoCommonValueError
        return a_key, b1

    raise TooManyCommonValuesError


def oddity_nb(iterable, key=None):
    summary = collections.defaultdict(list)
    for element in iterable:
        k = key(element) if key is not None else element
        summary[k].append(element)
    if len(summary) == 1:
        k, _ = summary.popitem()
        return k, None
    elif len(summary) == 2:
        common, different = list(summary.items())
        if len(common[1]) == 1:
            common, different = different, common
        return common[0], different[1][0]
    else:
        raise ValueError("Wrong number of distinct values")


class EmptyError(ValueError):

    pass


class TooManyDistinctValuesError(ValueError):

    pass


class TooManyCommonValuesError(ValueError):

    pass


class NoCommonValueError(ValueError):

    pass


class Tests(unittest.TestCase):

    def test_list(self):
        key, diff = oddity([1, 2, 1, 1])
        self.assertEqual(diff, 2)

    def test_list_empty(self):
        self.assertRaises(EmptyError, oddity, [])

    def test_list_all_the_same(self):
        key, diff = oddity([1, 1, 1, 1])
        self.assertEqual((key, diff), (1, None))

    def test_list_too_many_distinct(self):
        self.assertRaises(TooManyDistinctValuesError, oddity, [1, 2, 3])

    def test_list_too_many_common(self):
        self.assertRaises(TooManyCommonValuesError, oddity, [2, 1, 2, 1, 1])

    def test_str(self):
        key, diff = oddity('aaaaba')
        self.assertEqual((key, diff), ('a', 'b'))

    def test_str_empty(self):
        self.assertRaises(EmptyError, oddity, '')

    def test_str_all_the_same(self):
        key, diff = oddity('aaaaaa')
        self.assertEqual((key, diff), ('a', None))

    def test_str_too_many_distinct(self):
        self.assertRaises(TooManyDistinctValuesError, oddity, 'aaaaaabc')

    def test_with_key(self):
        items = [10, 11, 12, 23, 14, 10]
        key, diff = oddity(items, key=lambda v: v // 10)
        self.assertEqual((key, diff), (1, 23))

    def test_one_of_each(self):
        self.assertRaises(NoCommonValueError, oddity, 'ab')

    def test_two_of_each(self):
        self.assertRaises(TooManyCommonValuesError, oddity, 'abab')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(oddity(sys.argv[1]))
    else:
        s = ['1'] * 100
        s[-1] = '0'
        print(timeit.timeit('oddity(s)', number=100000, globals=globals()))
        print(timeit.timeit('oddity_groupby(s)', number=100000, globals=globals()))
        print(timeit.timeit('oddity_nb(s)', number=100000, globals=globals()))
