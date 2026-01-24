def PrintBinary(no):
    if no == 0:
        return "0"
    binary = ""
    while no > 0:
        binary = str(no % 2) + binary
        no //= 2
    return binary



def main():
    no = int(input("Enter a number: "))
    print("Binary Equivalent: ",PrintBinary(no))
    

if __name__=="__main__":
    main()