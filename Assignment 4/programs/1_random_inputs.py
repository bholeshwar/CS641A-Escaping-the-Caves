import random

def random_32():
    s = ""

    for i in range(32):
        s += str(random.randint(0,1))

    return s


random_inputs = []

for i in range(10):
    L = random_32()
    L1 = random_32()
    R = random_32()

    random_inputs.append(L + R)
    random_inputs.append(L1 + R)

for i in random_inputs:
    print i
