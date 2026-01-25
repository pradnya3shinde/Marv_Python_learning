from functools import reduce

Add=lambda a,b: a+b

def main():
    data=[9,10,15,21,34,79,60]
    print("Actual Data is: ",data)

    RData=reduce(Add,data)
    print("Data after reduce is : ",RData)

if __name__=="__main__":
    main()