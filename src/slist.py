__all__ = ['cons', 'slist', 'nil']

class EmptyList:
    def __iter__(self):
        return iter(())

    def __bool__(self):
        return False

    def __len__(self):
        return 0

    def __repr__(self):
        return 'nil'

nil = EmptyList()

class ConsCell:
    def __init__(self, hd, tl=nil):
        self.hd = hd
        self.tl = tl

    def __iter__(self):
        tmp = self
        while tmp is not nil:
            yield tmp.hd
            tmp = tmp.tl

    def __eq__(self, other):
        if not hasattr(other, 'hd') or self.hd != other.hd:
            return False
        # FIXME: no TCO in Python
        return self.tl == other.tl

    def __hash__(self):
        result = id(nil)
        for elem in self:
            result ^= hash(elem)
        return result

    def __repr__(self):
        return 'slist(%r)' % list(self)

    def __reversed__(self):
        return rev_slist(self)

    def __len__(self):
        result = 0
        for _ in self:
            result += 1
        return result

cons = ConsCell

def slist(elems=()):
    return rev_slist(reversed(elems))

def rev_slist(elems):
    result = nil
    for elem in elems:
        result = cons(elem, result)
    return result
