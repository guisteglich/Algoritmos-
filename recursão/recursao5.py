'''
Defina a função div que recebe como argumentos dois números naturais  m  e  n  
e devolve o resultado da divisão inteira de  m  por  n.'''

def div(m, n):
    if n == 0:
        return 0
    else:
        return n + div(m, n-1)

print(div())