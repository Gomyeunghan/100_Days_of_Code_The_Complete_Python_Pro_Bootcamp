from collections import defaultdict

import art
#
# def add(n1, n2):
#     return n1 + n2
# def subtract(n1 , n2):
#     return n1 - n2
# def multiply(n1 , n2):
#     return n1 * n2
# def divide(n1 , n2):
#     return n1 / n2
#
# def calculator (n1, n2 ,operator ):
#     result = 0
#     if operator == "+":
#         result = add(n1, n2)
#         print(f'{n1} + {n2} = {result}')
#         return result
#     if operator == "-":
#         result = subtract(n1, n2)
#         print(f'{n1} + {n2} = {result}')
#         return result
#     if operator == "*":
#         result = multiply(n1, n2)
#         print(f'{n1} + {n2} = {result}')
#         return result
#     if operator == "/":
#         result = divide(n1, n2)
#         print(f'{n1} + {n2} = {result}')
#         return result


# def adove_average(number):
#     bigger_avg = []
#     avg = sum(number) / len(number)
#     for num in number:
#         if num > avg:
#             bigger_avg.append(num)
#     return bigger_avg
#
# def total_price(orders_list):
#     total_price_dic = {}
#     for order in orders_list:
#         for product in order:
#             order[product] = order["".


def classify(text):
    output = {}
    if "배송" in text or "언제 오나요" in text:
        output = {'type': "배송문의" , 'input' : text }
        print(output)
        return output
    elif "환불" in text or "취소" in text:
        output =  {'type': "환불문의", 'input': text}
        print(output)
        return output
    elif "재고" in text or "품절" in text:
        output = {'type': "재고문의", 'input': text}
        print(output)
        return output
    else:
        output = {'type' : '기타' , 'input' : text}
        print(output)
        return output


classify("사이즈가 커요")



#
# print(art.logo)
#
# continue_calc = ''
# calc_num = 0
#
# while True:
#     if continue_calc == "y":
#         calc_num = calculator(n1=calc_num,
#                               operator=str(input("+\n-\n*\n/\nPick an operation: ")),
#                               n2=int(input("What is the second number?: ")))
#         continue_calc = input(
#             f"Type 'y' to continue calculating with {calc_num} or type 'n' to start a new calculation: ")
#     else :
#         print('\n' * 100)
#         print(art.logo)
#         calc_num = calculator(n1=int(input("What is the firest number?: ")),
#                               operator=str(input("+\n-\n*\n/\nPick an operation: ")),
#                               n2=int(input("What is the second number?: ")))
#         continue_calc = input(
#             f"Type 'y' to continue calculating with {calc_num} or type 'n' to start a new calculation: ")
#
#
