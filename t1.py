def fizzBuzz(n):
    for elem in range(1, n+1):
        print(f'esse é o elemento {elem}:', elem % 3)
        if ((elem % 3 == 0) and (elem % 5 == 0)):
            print("FizzBuzz")
        elif (elem % 3 == 0):
            print("Fizz")
        elif (elem % 5 == 0):
            print("Buzz")
        else:
            print(elem)
        
print(fizzBuzz(15))