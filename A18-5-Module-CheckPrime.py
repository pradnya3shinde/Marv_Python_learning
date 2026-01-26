import ArithMatic

def ListPrime(no):
    lst=[]
    for i in range(no):
        lst.append(int(input("Enter number:")))

    sum=0   
    for i in lst:
        if ArithMatic.ChkPrime(i):
            sum+=i
    print("Addition of prime numbers from list: ",sum)


def main():
    n = int(input("Enter how many number you want to enter: "))
    ListPrime(n)
    

if __name__=="__main__":
    main()