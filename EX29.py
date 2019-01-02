def count_spaces(userInput):
    spaces = 0
    for char in userInput:
        if char == " ":
            spaces = spaces + 1
    return spaces

def main():
    information = input("Please enter  any information:")
    print("Number of spaces in your input is:", \
count_spaces(information))

main()
