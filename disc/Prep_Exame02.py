'''recursion fill-in, tree recusion fill-in '''

def print_numbers(n, k):
    """Print all numbers that (A) can be formed from the digits
    of `n` in reverse order and (B) are multiples of `k`.
    This is essentially Fall 2015 Midterm 2 #3c written to not
    depend on knowledge of lists.
    Args:
    n (int): The number that results must use digits from.
    k (int): The number that results must be multiples of.
    >>> print_numbers(97531, 5)
    135
    15
    35
    >>> print_numbers(97531, 7)
    1379
    357
    35
    >>> print_numbers(97531, 2)
    """

    def inner(n, s):
        if n == 0:
            if s % k == 0 and s > 0:
                print(s)
        else:
            inner(n // 10, s * 10 + n % 10)  # first
            inner(n // 10, s)  # second why need this guy??

    inner(n, 0)
    #https://stackoverflow.com/questions/53602008/double-recursive-call
    #这个跑出来答案里面会有个位数5


def sixty_ones(n):
    """Return the number of times that a 1 directly follows a 6
    in the digits of `n`.
    This is essentially Fall 2014 Midterm 2 #3a written to not
    depend on knowledge of lists.
    Args:
    n (int): The number whose digits are to be examined.
    Returns:
    int: The number of occurrences.
    >>> sixty_ones(461601)
    1
    >>> sixty_ones(161461601)
    2
    """
    if n < 10:
        return 0
    elif n % 10 == 1 and n // 10 % 10 == 6:
        return 1 + sixty_ones(n//10)
    else:
        return sixty_ones(n//10)

def no_elevens(n):
    """Return the number of `n`-digit numbers whose digits
    consist of 1's and 6's and do not contain a `1` and
    then another `1` consecutively.
    This is essentially Fall 2014 Midterm 2 #3b rewritten to
    not depend on knowledge of lists.
    Args:
    n (int): The length of the numbers.
    Returns:
    int: The number of numbers.
    >>> no_elevens(2) # 66, 61, 16
    3
    >>> no_elevens(3) # 666, 661, 616, 166, 161
    5
    """
    if n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        return no_elevens(n - 1) + no_elevens(n - 2)
    # here I didn't consider the case n<2

print(no_elevens(6))