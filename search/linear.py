def linear(elem, arr):
    for i in range(len(arr)):
        if arr[i] == elem:
            return i, elem
    return False

arr = [1, 3, 5]
print(linear(5, arr))