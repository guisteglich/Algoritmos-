def pot(n, p):
    if p == 0:
        return 1
    else:
        return n * pot(n, p-1)

print(pot(60, 5))
