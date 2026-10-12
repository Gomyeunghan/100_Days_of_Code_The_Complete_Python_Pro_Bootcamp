
try:
    age = int(input("What's your age?"))
except ValueError:
    print("You have entered an invalid age.")
    age = int(input("How old are you?"))

print(f"You can drive at age {age}.")
