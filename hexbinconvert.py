#hexstring.py cwc
def bincon(decimal):
    bin_str = ""
    for i in range(8):
        binary = str(decimal % 2)
        decimal = decimal // 2
        bin_str = bin_str + str(binary)
    return bin_str[::-1]

def hexcon(decimal):
    hexstring = ""
    #remainder = str(decimal % 16)
    if (decimal % 16 > 9):
        addasc = 55
    else:
        addasc = 48
    remainder =  str(chr((decimal % 16)+addasc))
    # ***********************************
    if (decimal // 16 > 9):
        addasc = 55
    else:
        addasc = 48
    quotient =  str(chr((decimal // 16)+addasc))
    hexstring = quotient+remainder
    # ***********************************
    return hexstring

def main():
    print("INPUT -1 TO EXIT THE PROGRAM")
    print("INPUT A POSITIVE INTEGER LESS THAN 256")
    done = 0
    while (done >= 0):
        dec = int(input("INPUT AN INTEGER : "))
        hexs = hexcon(dec)
        bins = bincon(dec)
        print(dec,hexs,bins)
        done = dec

main()
