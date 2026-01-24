# syntas lambda parameters: function body
IsDivBy5=lambda No:(No%5==0) 

def main():
    value=int(input("Enter number: "))
    ret=IsDivBy5(value)
    if ret ==True:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")



if __name__=="__main__":
    main()