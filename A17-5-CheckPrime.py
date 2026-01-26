 

def CheckPrime(no):
    if no <= 1:
        print("Not a Prime Number")
    else:
        for i in range(2, int(no**0.5) + 1):
         if no % i == 0:
            print("Not a Prime Number")
            break
        else:
            print("Prime Number")


def main():
    no=int(input("Enter number: "))
    CheckPrime(no)
    

if __name__=="__main__":
    main()