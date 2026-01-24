# syntas lambda parameters: function body
FindLargestNum = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)

def main():
    no1=int(input("Enter 1st number: "))
    no2=int(input("Enter 2nd number: "))
    no3=int(input("Enter 3rd number: "))
    ret=FindLargestNum(no1,no2,no3)
    print("Largest Number is",FindLargestNum(no1,no2,no3))

if __name__=="__main__":
    main()