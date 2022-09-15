def sum_arr(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_arr(arr[1:])

arr = [1, 3, 5, 1, 4, 6]
print(sum_arr(arr))
