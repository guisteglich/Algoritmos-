def inverse(arr):
    array_inverted = []
    for i in arr[::-1]:
        array_inverted.append(i)
    return array_inverted

def inverse2(arr):
    n = len(arr)-1
    for i in range(0, len(arr)//2):
        aux = arr[i]
        arr[i] = arr[n]
        arr[n] = aux
        n-=1
    return arr

arr = [1, 5, 7, 2, 3]
print("array original: ", arr)
print(inverse(arr))
print(inverse2(arr))