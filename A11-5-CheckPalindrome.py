 

def CheckPalindrome(n):
    rev = 0
    originalNum=n

    while n > 0:
        digit = n % 10   
        rev=rev*10+digit    
        n = n // 10  
    print("Reversed number is:", rev)

    if originalNum == rev:
        print("Number is a palindrome")
    else:
        print("Number is not a palindrome")


def main():
    no=int(input("Enter number: "))
    CheckPalindrome(no)
    

if __name__=="__main__":
    main()