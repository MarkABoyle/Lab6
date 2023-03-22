# Mark Boyle
from encoderdecoder2 import decode


def encode(password):
    listpass = list(password)
    for i in range(0, len(listpass)):
        listpass[i] = str(int(listpass[i]) + 3)
        if int(listpass[i]) >= 10:
            listpass[i] = str(int(listpass[i]) - 10)
        else:
            continue
    newlist = ''.join(listpass)
    return newlist


def main():
    saved_pass = ''
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        menu_input = input("Please enter an option: ")
        if menu_input == '1':
            saved_pass = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif menu_input == '2':
            if saved_pass != '':
                print(f"The encoded password is {saved_pass}, and the original password is {decode(saved_pass)}.")
            else:
                print("No Password Input to Decode.")
        elif menu_input == '3':
            exit(0)
        else:
            print("Invalid Input\n")


main()
