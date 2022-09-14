from itertools import count
from operator import le


def aVeryBigSum(ar):
    count_f = 0
    for i in range(0, len(ar)):
        count_f += ar[i]
    return count_f

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(ar))