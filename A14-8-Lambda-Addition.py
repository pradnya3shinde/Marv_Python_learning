# syntas lambda parameters: function body
Addition=lambda no1,no2: no1 + no2

def main():
    no1=int(input("Enter 1st number: "))
    no2=int(input("Enter 2nd number: "))
    ret=Addition(no1,no2)
    print("Addition of two numbers is",Addition(no1,no2))

if __name__=="__main__":
    main()