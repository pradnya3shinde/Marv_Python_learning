# syntas lambda parameters: function body
CheckOdd=lambda No:(No%2==1) 

def main():
    value=int(input("Enter number: "))
    ret=CheckOdd(value)
    if ret ==True:
        print("True: It is Odd number")
    else:
        print("False: It is not odd number") 


if __name__=="__main__":
    main()