#Q2-2
h = float(input('Height(m) = '))
w = float(input('Weight(kg) = '))

bmi = w / (h ** 2)
print(round(bmi, 2))

if bmi > 18.5 :
    print('skinny')
elif 18.5 <= bmi < 25 :
    print('normal')
elif  25 <= bmi < 35 :
    print('a little fat')
else :
    print('fat')

