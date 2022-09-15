def arrayManipulation(n, queries):
    arr = [0 for i in range(n)]
    A = [queries]
    for i in range(len(queries)):
        for j in range(queries[i][0] - 1, queries[i][1]):
            arr[j] = arr[j] + queries[i][2]
    return(max(arr))

arr = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
print(arrayManipulation(10, arr))