import AssignmentLibrary

def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area= AssignmentLibrary.Rectangle_area(length,width)
    print("Area of rectangle =", area)
    

if __name__=="__main__":
    main()