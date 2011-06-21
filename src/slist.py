__all__ = ['cons', 'slist', 'nil']

class ConsCell:
    def __init__(self, hd, tl):
        self.hd = hd
        self.tl = tl

    def __iter__(self):
        tmp = self
        while tmp is not nil:
            yield tmp.hd
            tmp = tmp.tl

    def __repr__(self):
        return 'slist(%r)' % list(self)

class EmptyList:
    def __iter__(self):
        return iter(())

    def __bool__(self):
        return False

    def __repr__(self):
        return 'nil'

cons = ConsCell
nil = EmptyList()

def slist(elems):
    result = nil
    for elem in reversed(elems):
        result = cons(elem, result)
    return result
