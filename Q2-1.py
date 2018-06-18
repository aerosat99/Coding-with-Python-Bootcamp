#Q2-1
def fizzbuzz(a) :
    if a % 15 == 0 :
        return 'FizzBuzz'
    elif a % 3 == 0 :
        return 'Fizz'
    elif a % 5 == 0 :
        return 'Buzz'
    else :
        return a

k = int(input('int = '))
for v in range(1, k+1) :
    print(fizzbuzz(v))