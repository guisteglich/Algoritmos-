'''
Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
For example, the super digit of 9875  will be calculated as:
'''
def superDigit(n, k):
    digit=str(n)
    li=list(map(int,digit))
    if sum(li)*k<10:
        return sum(li)
    else:
        return superDigit(sum(li)*k,1)

print(superDigit('9875', 4))

# def superDigit(n, k):
#     if(len(n)==1 and k==1):
#         return int(n)
#     else:
#         suma = sum(list(map(int,n)))
#         return superDigit(str(suma*k),1)




