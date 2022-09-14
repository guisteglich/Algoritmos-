# def insertionSort1(n, arr):
#     aux = arr[-1]
#     # arr[-1] = arr[-2]
#     for i in range(n-1):
#         if arr[i] > aux:
#             arr[i+1] = arr[i]
#             arr[i] = aux
#     return arr
#     # Write your code here

def insertionSort1(n, arr):
    t = arr[n-1]
    k = n-2
    while k >= 0 and t < arr[k]:
        arr[k+1] = arr[k]
        s = str(arr)[1:-1].replace(",", "")
        print(s)
        k -= 1
    arr[k+1] = t
    s = str(arr)[1:-1].replace(",", "")
    print(s)
        


arr1= [2, 4, 6, 8, 3]
arr = [1, 2, 4, 5, 3]
print(insertionSort1(5, arr))
