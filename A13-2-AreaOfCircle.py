import AssignmentLibrary

def main():
    radius = float(input("Enter radius: "))
    area= AssignmentLibrary.Rectangle_Circle(radius)
    print("Area of Circle =", area)
    

if __name__=="__main__":
    main()