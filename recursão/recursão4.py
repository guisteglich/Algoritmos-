'''Defina a função soma_nat que recebe como argumento 
um número natural  n e devolve a soma de todos 
os números naturais até  n .'''

def soma_nat(n):
    if n <= 1:
        return n
    else:
        return n + soma_nat(n-1)

print(soma_nat(5))