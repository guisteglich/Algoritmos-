def max_sum_subarray(arr):
    max_now = 0
    max_end = 0
    for i in range(0, len(arr)):
        max_now += arr[i]
        if max_now < max_end:
            max_now = max_end
        if max_end < 0:
            max_end = 0
    return max_now

arr = [1, 2, 3, -4, 6]
print(max_sum_subarray(arr))
