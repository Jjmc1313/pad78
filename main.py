import random
import math

ende = input("Do you want to encode or decode? (E/D) ")

if ende == "E":
    key = input("Do you want to use a pre-existing key? (Y/N) ")
    if key == "Y":
        ekey = input("Input Your Key: ")  # saves custom key
        print("")
        msg = input("Message String: ")  # this is the message that is encrypted

        binary = ''.join(format(ord(i), '08b') for i in msg)  # converts the message into 8-bit binary

        len_bin = len(binary)  # measures the length of the binary
        mult7 = math.ceil(len_bin / 7) * 7  # finds the next multiple of 7 after the length of the binary
        padsize = mult7 - len_bin  # finds the difference between length of binary and length of next multiple of 7
        padding = "".join(["0"] * padsize)  # adds the correct amount of zeros to end of 8 bit binary for 7 divisibility
        paddingend = "".join(["§"] * padsize)  # does the same thing as the above, except this is added to the
        # end result
        padded = binary + padding  # actually creates a variable where the zeros are added to the binary

        sep = " ".join(padded[i:i + 7] for i in range(0, len(padded), 7))  # splits the new 8-bit padded binary into
        # bytes of 7
        print(sep)

        data = sep.split()
        data = [int(x, 2) for x in data]  # converts the 7-bit binary data into raw decimal numbers and prints in array
        print(data)

        string = str(ekey)  # uses the inputted key as a "decoding wheel"
        for x in data:
            if x >= 77:
                print(string[x % 77], end=" ")  # if a number in the above array is larger than 77, subtract 77 and pull
                # that number from the "decoding wheel", then add a space afterwards to signify it
            else:
                print(string[x % 77], end='')  # if the number is not larger than 77, pull from wheel and continue on
        print(paddingend)  # adds the symbols to represent the original padding number

    if key == "N":
        chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=[];',./_+{}|:"<>?"""

        randkey = ("".join(random.sample(chars, 77)))  # randomly organizes the above list into 77 character code
        print("[" + randkey + "]" + " Is Your New Key!")

        print("")
        msg = input("Message String: ")  # this is the message that is encrypted

        binary = ''.join(format(ord(i), '08b') for i in msg)  # converts the message into 8-bit binary

        len_bin = len(binary)  # measures the length of the binary
        mult7 = math.ceil(len_bin / 7) * 7  # finds the next multiple of 7 after the length of the binary
        padsize = mult7 - len_bin  # finds the difference between length of binary and length of next multiple of 7
        padding = "".join(["0"] * padsize)  # adds the correct amount of zeros to end of 8 bit binary for 7 divisibility
        paddingend = "".join(["§"] * padsize)  # does the same thing as the above, except this is added to the
        # end result
        padded = binary + padding  # actually creates a variable where the zeros are added to the binary

        sep = " ".join(padded[i:i + 7] for i in range(0, len(padded), 7))  # splits the new 8-bit padded binary into
        # bytes of 7
        print(sep)

        data = sep.split()
        data = [int(x, 2) for x in data]  # converts the 7-bit binary data into raw decimal numbers and prints in array
        print(data)
        print(data)

        string = str(randkey)  # uses the inputted key as a "decoding wheel"
        for x in data:
            if x >= 77:
                print(string[x % 77], end=" ")  # if a number in the above array is larger than 77, subtract 77 and pull
                # that number from the "decoding wheel", then add a space afterwards to signify it
            else:
                print(string[x % 77], end='')  # if the number is not larger than 77, pull from wheel and continue on
        print(paddingend)  # adds the symbols to represent the original padding number

if ende == "D":
    rmsg = input("Enter your received message: ")
    rkey = input("Enter your received key: ")

