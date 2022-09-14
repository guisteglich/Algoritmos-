def introTutorial(V, arr):
    for i in range(len(arr)):
        if arr[i] == V:
            return i

arr = [1, 4, 5, 7, 9, 12]
print(introTutorial(4, arr))