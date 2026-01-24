 

def ReverseNum(n):
    rev = 0

    while n > 0:
        digit = n % 10   
        rev=rev*10+digit    
        n = n // 10  
    print("Reversed number is:", rev)


def main():
    no=int(input("Enter number: "))
    ReverseNum(no)
    

if __name__=="__main__":
    main()