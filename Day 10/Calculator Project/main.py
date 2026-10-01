import art

def add(n1, n2):
    return n1 + n2
def subtract(n1 , n2):
    return n1 - n2
def multiply(n1 , n2):
    return n1 * n2
def divide(n1 , n2):
    return n1 / n2

def calculator (n1, n2 ,operator ):
    result = 0
    if operator == "+":
        result = add(n1, n2)
        print(f'{n1} + {n2} = {result}')
        return result
    if operator == "-":
        result = subtract(n1, n2)
        print(f'{n1} + {n2} = {result}')
        return result
    if operator == "*":
        result = multiply(n1, n2)
        print(f'{n1} + {n2} = {result}')
        return result
    if operator == "/":
        result = divide(n1, n2)
        print(f'{n1} + {n2} = {result}')
        return result


print(art.logo)

continue_calc = ''
calc_num = 0

while True:
    if continue_calc == "y":
        calc_num = calculator(n1=calc_num,
                              operator=str(input("+\n-\n*\n/\nPick an operation: ")),
                              n2=int(input("What is the second number?: ")))
        continue_calc = input(
            f"Type 'y' to continue calculating with {calc_num} or type 'n' to start a new calculation: ")
    else :
        print('\n' * 100)
        print(art.logo)
        calc_num = calculator(n1=int(input("What is the firest number?: ")),
                              operator=str(input("+\n-\n*\n/\nPick an operation: ")),
                              n2=int(input("What is the second number?: ")))
        continue_calc = input(
            f"Type 'y' to continue calculating with {calc_num} or type 'n' to start a new calculation: ")