'''
Dado um array de inteiros e o seu número
de elementos, inverta a posição dos seus
elementos
'''

def rec(arr, n):
    if n <= 1:
        return arr
    else:
        return arr[::-1]

print(rec([1, 4, 7], 3))