from functools import reduce

CheckEven = lambda no:(no%2==0) 


def main():
    data=[7,90,13,60,22,56,40]
    print("Actual Data is: ",data)

    FData=list(filter(CheckEven,data))
    print("Data after filter is : ",FData)


if __name__=="__main__":
    main()