from functools import reduce

max=lambda a, b: a if a > b else b

def main():
    data=[7,90,13,60,22,56,40]
    print("Actual Data is: ",data)

    RData=reduce(max,data)
    print("Data after reduce, Maximum number is : ",RData)

if __name__=="__main__":
    main()