class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3, 4, 5>
    >>> s.second
    4
    >>> s.first = 6
    >>> s.second = 7
    >>> s.rest.rest = Link.empty
    >>> s
    Link(6, Link(7))
    >>> print(s.rest)
    <7>
    >>> Link(1, Link(Link(2, Link(3)), Link(4)))
    Link(1, Link(Link(2, Link(3)), Link(4)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


# def multiply_lnks(lst_of_lnks):
#     """
#     >>> a = Link(2, Link(3, Link(5)))
#     >>> b = Link(6, Link(4, Link(2)))
#     >>> c = Link(4, Link(1, Link(0, Link(2))))
#     >>> p = multiply_lnks([a, b, c])
#     >>> p.first
#     48
#     >>> p.rest.first
#     12
#     >>> p.rest.rest.rest
#     ()
#     """
#     k = 1
#     if Link.empty in lst_of_lnks:
#         return Link.empty
#     for i in lst_of_lnks:
#
#         k *= i.first
#
#     restlinks = [i.rest for i in lst_of_lnks]
#     out = Link(k, multiply_lnks(restlinks))
#     return out


# def remove_duplicates(lnk):
#     """
#     >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
#     >>> remove_duplicates(lnk)
#     >>> lnk
#     Link(1, Link(5))
#     """
#     # not working
#     # pool = Link.empty
#     # while lnk is not Link.empty or lnk.rest is not Link.empty:
#     #     # print(lnk.first)
#     #
#     #     # lnk = lnk.rest
#     #     if lnk.first in pool:
#     #         lnk = lnk.rest.rest
#     #     else:
#     #         lnk = lnk.rest
#     #
#     #     pool.append(list(lnk[0]))
#------------------------------
    # solution iteration
    # while lst is not Link.empty or lst.rest is not Link.empty:
    #     if lst.first == lst.rest.first:
    #         lst.rest = lst.rest.rest
    #     else:
    #         lst = lst.rest

    #solution recution
    # if lnk == Link.empty or lnk.rest == Link.empty:
    #     return
    # if lnk.first == lnk.rest.first:
    #     lnk.rest = lnk.rest.rest
    #     remove_duplicates(lnk)
    # else:
    #     remove_duplicates(lnk.rest)

# def even_weighted(lst):
#     """
#     >>> x = [1, 2, 3, 4, 5, 6]
#     >>> even_weighted(x)
#     [0, 6, 20]
#     """
#     return [i * lst[i] for i in range(len(lst)) if i % 2 == 0]


# def quicksort_list(lst):
#     """
#     >>> quicksort_list([3, 1, 4, 2, 5, 6])
#     [1, 2, 3, 4, 5, 6]
#     """
#     if not lst or len(lst) == 1:
#         return lst
#     pivot = lst[0]
#     less = [i for i in lst if i < pivot]
#     greater = [i for i in lst if i > pivot]
#     return quicksort_list(less) + [pivot] + quicksort_list(greater)

# def max_product(lst):
#     """Return the maximum product that can be formed using lst
#     without using any consecutive numbers
#     >>> max_product([10,3,1,9,2]) # 10 * 9
#     90
#     >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
#     125
#     >>> max_product([])
#     1
#     """
#     # if not lst:
#     #     return 1
#     # elif len(lst) == 1:
#     #     return lst[0]
#     # max(lst[0] * max_product(lst[2:]), max_product(lst[1:]))
#
#     if not lst:
#         return 1
#     elif len(lst) == 1:
#         return lst[0]
#     else:
#         return  max(max_product(lst[1:]), lst[0] * max_product(lst[2: ]))

def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> redundant_map(tree, double)
    >>> print_levels(tree)
    [2] # 1 * 2 ˆ (1) ; Apply double one time
    [4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times [16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
    [256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
    """
    t.label = f(t.label)
    new_f = lambda x: f(f(x))
    for branch in t.branches:
        redundant_map(branch, new_f)