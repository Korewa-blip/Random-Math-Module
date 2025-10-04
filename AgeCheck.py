age_input = input("Enter your age: ")
if age_input.isdigit():
    age = int(age_input)
    print(f"Your age is",age)
else:
    print("Invalid age")
