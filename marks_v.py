def encode(password):
    listpass = list(password)
    for i in range(0, len(listpass)):
        listpass[i] = str(int(listpass[i]) + 3)
        if int(listpass[i]) > 10:
            listpass[i] = str(int(listpass[i])-10)
    newlist = ''.join(listpass)
    return newlist


def decode(encoded):
    listencode = list(encoded)
    for i in range(0, len(listencode)):
        listencode[i] = str(int(listencode[i]) - 3)
        if int(listencode[i]) < 0:
            listencode[i] = str(int(listencode[i]) + 10)
        else:
            continue
    newlist = ''.join(listencode)
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


# main()

print(decode("2289173"))