 

def SumOfDigits(n):
    sum = 0

    while n > 0:
        digit = n % 10   
        sum += digit    
        n = n // 10  

    print("Sum of digits is:", sum)


def main():
    no=int(input("Enter number: "))
    SumOfDigits(no)
    

if __name__=="__main__":
    main()