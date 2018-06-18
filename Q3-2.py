list1 = list(range(1,12))

for i in list1 :
    for j in list1 :
        print(i * j, end = ' ') # 각 단안에서는 줄 바꾸지 않고 옆으로 나열
    print(' ') # 한 단 끝나면 줄 바꿈