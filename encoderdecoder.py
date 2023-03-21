def encode(password):
    listpass = list(password)
    for i in range(0, len(listpass)):
        listpass[i] = str(int(listpass[i]) + 3)
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
            password = input("Please enter your password to encode: ")
            saved_pass = encode(password)
            # print(saved_pass)
        elif menu_input == '2':
            if saved_pass != '':
                print(saved_pass)
            else:
                continue
        elif menu_input == '3':
            exit(0)
        else:
            print("Invalid Input\n")


main()
