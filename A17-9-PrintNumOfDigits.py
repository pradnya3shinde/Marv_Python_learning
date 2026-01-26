 
def CountOfDigits(no):
    count = 0

    while no > 0:
        count += 1
        no //=10

    print("Number of digits =", count)


def main():
    no=int(input("Enter number: "))
    CountOfDigits(no)
    

if __name__=="__main__":
    main()