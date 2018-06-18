import random

def make_random_list(size) :
    list1 = []
    for v in range(size) :
        list1.append(random.randint(0,100))
    return list1

size = input('정수 입력 = ')
result = make_random_list(int(size))
print(result)