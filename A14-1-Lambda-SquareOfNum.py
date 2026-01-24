# syntas lambda parameters: function body
Square= lambda no: no*no

def main():
    value=int(input("Enter number: "))
    ret =Square(value)
    print("Sqaure of Number :",ret)


if __name__=="__main__":
    main()