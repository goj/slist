from nose.tools import assert_equal, assert_true, assert_false
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
