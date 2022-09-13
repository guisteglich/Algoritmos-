'''
calcule a soma de
todos os valores de um array de reais
'''

def rec(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + rec(arr[1:len(arr):1])
l = [1,3.0, 5.1]
print(rec(l))