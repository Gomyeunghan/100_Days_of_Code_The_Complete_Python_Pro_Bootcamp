year = int(input("What's your year of birth?"))

try:
    age = int(input("What's your age?"))
except ValueError:
    print("Please enter a valid age")
    age = int(input("What's your age?"))

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
