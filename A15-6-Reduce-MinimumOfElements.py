from functools import reduce

min=lambda a, b: a if a < b else b

def main():
    data=[7,90,13,60,22,56,40,-7]
    print("Actual Data is: ",data)

    RData=reduce(min,data)
    print("Data after reduce, Minimum number is : ",RData)

if __name__=="__main__":
    main()