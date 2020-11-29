# Write a program that asks the user to type a number.
# Convert the number to an integer and print it.
# If you can't convert their input to an integer, print a message that says "Please type an integer."

a = input("enter a number: ")
try:
    print(int(a))
except ValueError:
    print("Please type an integer.")
