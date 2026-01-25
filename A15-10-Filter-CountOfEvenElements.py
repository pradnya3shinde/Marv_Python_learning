from functools import reduce

CountOfEvenNums= lambda a:a%2==0


def main():
    data=[10,5,3,4,20]
    print("Actual Data is: ",data)

    FData=list(filter(CountOfEvenNums,data))
    print("Count of all even elements  : ",len(FData))


if __name__=="__main__":
    main()