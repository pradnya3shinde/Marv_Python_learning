from functools import reduce

LengthOfString=lambda x: len(x) > 5

def main():
    data=["python","ML", "Hell0","jayganesh", "Pradnya", "AIAndML", "Development"]
    print("Actual Data is: ",data)

    FData=list(filter(LengthOfString,data))
    print("Data after filter, String lenth is greater than 5  : ",FData)


if __name__=="__main__":
    main()