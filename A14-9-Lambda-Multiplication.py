# syntas lambda parameters: function body
Multiplication=lambda no1,no2: no1 * no2

def main():
    no1=int(input("Enter 1st number: "))
    no2=int(input("Enter 2nd number: "))
    ret=Multiplication(no1,no2)
    print("Multiplication of two numbers is",Multiplication(no1,no2))

if __name__=="__main__":
    main()