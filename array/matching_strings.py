from itertools import count


def matching_strings(arr, mstr):
    count_match = []
    for i in mstr:
        count = 0
        c = 0
        while c <len(arr):
            if i == arr[c]:
                count+=1
            c+=1
        count_match.append(count)
    return count_match

arr = ['ab', 'ab', 'abc']
mstr = ['ab', 'abc', 'bc']
print(matching_strings(arr, mstr))