CheckDiv3And5= lambda no : no%3==0 and no%5==0


def main():
    data=[7,90,13,60,22,56,40]
    print("Actual Data is: ",data)

    FData=list(filter(CheckDiv3And5,data))
    print("Numbers which are divisible by 3 and 5  : ",FData)


if __name__=="__main__":
    main()