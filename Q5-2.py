def get_sum(**kwargs) :
    start = kwargs['start']
    end = kwargs['end']
    result = 0
    for v in range(start, end+1) :
        result += v
    return result

s = int(input('int : '))
e = int(input('int : '))

val = get_sum(start = s, end = e)
print(val)