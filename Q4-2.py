def game_369(v) :
    if v % 3 == 0 :
        return 'Three'
    elif '3' in str(v) :
        return 'Three'
    else :
        return v

k = int(input('Max = '))

list1 = list(range(1, k+1))

for v in list1 :
    result = game_369(v)
    print(result)
