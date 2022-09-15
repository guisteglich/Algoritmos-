def equalStacks(h1, h2, h3):
    if len(h1, h2, h3) < 3:
        minimo = min(h1, h2, h3)
    

    return
    # Write your code here

h1 = [1, 1, 1, 2, 3]
h2 = [2, 3, 4]
h3 = [1, 4, 1, 1]

# n1, n2, n3 = input()
# h1 = n1*[]
# h2 = n2*[]
# h3 = n3*[]

def read_stack():
    stack = [int(x) for x in input().split(' ')]
    stack = list(reversed(stack))
    sum_stack = set()
    psum = 0
    for i in range(len(stack)):
        psum += stack[i]
        sum_stack.add(psum)
    return sum_stack

input()

ans = read_stack()
ans &= read_stack()
ans &= read_stack()
if len(ans) > 0:
    print(max(ans))
else:
    print(0)