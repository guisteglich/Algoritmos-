'''
Implemente uma função recursiva que,
dados dois números inteiros x e n, calcula o
valor de xn.
'''
def rec(x, n):
    if x == 0 or n == 0:
        return 0
    else:
        return x + rec(x, n-1)

print(rec(10, 1))