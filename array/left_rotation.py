from this import d


def left_rotation(arr, d):
    return arr[d:] + arr[:d]

arr = [1, 2, 4, 6]
print(left_rotation(arr, 3))