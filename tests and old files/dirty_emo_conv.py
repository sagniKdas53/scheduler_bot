while True:
    inpi = input()
    for inf in inpi:
        val = ord(inf)
        he = hex(val)
        he = he.upper()
        spli = he.index('X')
        unic = he[spli + 1:]
        while len(unic) < 8:
            unic = '0' + unic
        unic = 'U' + unic
        print(inf, ' is ', unic)
        if inpi == '.':
            break
    if inf == '.':
        break
