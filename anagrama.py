def anagrama(p1, p2):
    if len(p1) != len(p2):
        return False
    else:
        p1 = list(p1)
        aux = 0
        for i in p1[::-1]:
            print(i)
            if i == p2[aux]:
                aux+=1
            else:
                return False
        return True


print(anagrama("marrocos", "socorran"))