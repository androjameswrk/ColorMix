print("Enter the colors that you want to mix.")
first_color = input("Enter first color: ").lower()
second_color = input("Enter second color: ").lower()

if (first_color == "red" and second_color == "blue") or (first_color == "blue" and second_color == "red"):
    print("red + blue = purple")
elif (first_color == "red" and second_color == "yellow") or (first_color == "yellow" and second_color == "red"):
    print("red + yellow = orange")
elif (first_color == "blue" and second_color == "yellow") or (first_color == "yellow" and second_color == "blue"):
    print("blue + yellow = green")
else:
    print("Invalid colors entered. Please enter red, blue, or yellow.")