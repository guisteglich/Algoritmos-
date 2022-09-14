# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    score = []
    ca = 0 
    cb = 0
    for i in range(0, len(a)): 
        if a[i] > b[i]:
            ca+=1
        elif a[i] < b[i]:
            cb+=1
    score.append(ca)
    score.append(cb)
            
    return score

a = [5, 6, 7]
b = [3, 6, 10]

print(compareTriplets(a, b))
            