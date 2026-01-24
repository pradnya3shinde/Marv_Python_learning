# syntas lambda parameters: function body
Cube= lambda no: no*no*no

def main():
    value=int(input("Enter number: "))
    ret =Cube(value)
    print("Cube of Number :",ret)


if __name__=="__main__":
    main()