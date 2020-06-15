import random
def adder(iteration):
    if iteration == 1:
        return 1
    print(random.randint(1,100) + adder(iteration-1))
    return random.randint(1,100) + adder(iteration-1)

adder(4)
