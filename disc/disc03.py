def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(i):
        if i == n :
            return True
        elif n % i == 0 or n == 1:
            return False
        else:
            return prime_helper(i + 1)
    return prime_helper(2)



    # m = 2
    # while m < n:
    #     if n == 2:
    #         return True
    #     elif n == 1:
    #         return True
    #     if n % m == 0:
    #         return False
    #     else:
    #         m = m + 1
    # return True

    # return is_prime(n)

def count_stair_ways(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return count_stair_ways(n-1) +count_stair_ways(n-2)

def count_k(n, k):
    if n == 0:
        return 1 #为啥这里是1？ 我之前填的0
    elif n == 1:
        return 1
    else:
        i = 1
        count_total = 0
        while i <= k and n > 0:
            count_total += count_k(n-i,k)
            i += 1
        return count_total

    #答案
    # if n == 0:
    #     return 1
    # elif n < 0:
    #     return 0
    # else:
    #     total = 0
    #     i = 1
    #     while i <= k:
    #         total += count_k(n - i, k)
    #         i += 1
    #     return total



def pascal(row, column):

    if column == 0:
        return 1
    elif row == 0:
        return 0 # why?!0 rather than 1
    else:
        return pascal(row-1, column) + pascal(row-1, column-1)

    #解2
    # if column == 0 or row == column:
    #     return 1
    # else:
    #     return pascal(row-1, column) + pascal(row-1, column-1)
