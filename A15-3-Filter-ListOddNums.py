from functools import reduce

CheckOdd = lambda no:(no%2==1) 


def main():
    data=[7,90,13,60,22,56,40]
    print("Actual Data is: ",data)

    FData=list(filter(CheckOdd,data))
    print("Data after filter is : ",FData)


if __name__=="__main__":
    main()