# syntas lambda parameters: function body
CheckEven=lambda No:(No%2==0) 

def main():
    value=int(input("Enter number: "))
    ret=CheckEven(value)
    if ret ==True:
        print("True: It is even")
    else:
        print("False: It is not even number") 


if __name__=="__main__":
    main()