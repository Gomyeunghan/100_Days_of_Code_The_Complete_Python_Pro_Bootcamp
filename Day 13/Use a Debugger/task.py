def fizz_buzz(target):
    target = int(target)
    for number in range(1, target+1 ):

        if  number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0 :
            print("Fizz")
        else:
            print([number])

fizz_buzz(15)