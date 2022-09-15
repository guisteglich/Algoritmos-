def soma_int(n):
    if n == 1:
        return 1
    else:
        return n + soma_int(n-1)

print(soma_int(5))
