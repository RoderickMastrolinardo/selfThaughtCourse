# Write a program with an infinite loop (with the option to type q to quit)
# and a list of numbers. Each time through the loop ask the user to guess a
# number on the list and tell them whether or not they guessed correctly.

numberList = [1, 2, 6, 8]
keep = True

while keep:
    userInput = input("guess a number(or type q to quit): ")
    print(userInput)
    if(userInput == "q" or userInput == "Q"):
        break
    if (int(userInput) in numberList):
        print("You guessed!")
    else:
        print("Wrong number :(")
