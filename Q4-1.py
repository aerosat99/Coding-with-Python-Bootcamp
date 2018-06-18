def compare_string(a, b) :
    if len(a) > len(b) :
        return a
    else :
        return b

k1 = input('1 = ')
k2 = input('2 = ')

result = compare_string(k1, k2)
print(result)