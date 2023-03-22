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
