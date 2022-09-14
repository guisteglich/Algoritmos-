# def diagonalDifference(arr):
#     dp = sum(arr[i][i] for i in range(len(arr)))
#     ds = 0
#     for j in arr[::-1]:
#         print(j[j])
#         # ds += arr[j][j]
#     final = dp - ds
#     return final

def diagonalDifference(arr):
    dp, ds = 0, 0
    # single pass, grab both values
    for i in range(len(arr)):
        dp += arr[i][i]
        ds += arr[i][-i-1]
    return abs(dp-ds)

"""
11 2 4
4 5 6
10 8 -12
"""
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))