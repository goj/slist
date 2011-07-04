from nose.tools import assert_true, assert_false
from nose.tools import assert_equal, assert_not_equal, assert_list_equal
from slist import cons, slist, nil

def test_cons():
    lst = cons(1, nil)
    assert_equal(lst.hd, 1)
    assert_equal(lst.tl, nil)

def test_slist():
    lst = slist([1, 2, 3])
    assert_equal(lst.hd, 1)
    assert_equal(lst.tl.hd, 2)
    assert_equal(lst.tl.tl.hd, 3)
    assert_equal(lst.tl.tl.tl, nil)

def test_iter():
    for lst in [ [], [1], [1, 2, 3], [1, 1, 1] ]:
        assert_equal(lst, list(slist(lst)))

def truth_test():
    assert_false(nil)
    assert_true(slist([1]))

def repr_test():
    assert_equal(repr(nil), 'nil')
    assert_equal(repr(slist([1, 2, 3])), 'slist([1, 2, 3])')

def test_no_arg_constructor():
    assert_true(slist() is nil)

def test_one_arg_constructor():
    lst = cons(1)
    assert_equal(lst.hd, 1)
    assert_equal(lst.tl, nil)

def equality_test():
    assert_equal(slist(), slist())
    assert_equal(slist([1]), slist([1]))
    assert_not_equal(slist([]), slist([1]))
    assert_not_equal(slist([1]), slist([]))
    assert_equal(slist([1, 2, 3]), slist([1, 2, 3]))
    assert_not_equal(slist([0, 2]), slist([1, 1]))
    assert_not_equal(slist([1, 2]), slist([1, 0]))
    assert_not_equal(slist([1, 2]), slist([1]))
    assert_not_equal(slist([1]), slist([1, 2]))

def hash_test():
    assert_equal(hash(slist()), hash(slist()))
    assert_equal(hash(slist([1])), hash(slist([1])))
    assert_equal(hash(slist([1, 2, 3])), hash(slist([1, 2, 3])))
    assert_not_equal(hash(slist()), hash(slist([1])))
    assert_not_equal(hash(slist([1, 2, 3])), hash(slist([1])))

def test_reversed():
    assert_equal(reversed(slist([1, 2, 3])), slist([3, 2, 1]))

def test_len():
    assert_equal(len(nil), 0)
    assert_equal(len(slist([1])), 1)
    assert_equal(len(slist([1, 2, 3])), 3)

def test_free_stuff():
    assert_equal(sum(slist([1, 2, 3])), 6)
    assert_equal(set(slist([1, 2, 1])), {1, 2})
    assert_equal(dict(slist([(1, 2), (3, 4)])), {1: 2, 3: 4})
