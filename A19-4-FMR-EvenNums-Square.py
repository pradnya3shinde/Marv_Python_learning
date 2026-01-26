from functools import reduce

def AcceptNumbers(no):
    lst=[]
    for i in range(no):
        lst.append(int(input("Enter number:")))
    return lst

Squares = lambda no:(no*no) 
FindEven=lambda no: no%2==0
ProductOfAll= lambda a,b : a*b

def main():
    n = int(input("Enter how many number you want to enter: "))
    listVal=AcceptNumbers(n)
    
    FData=list(filter(FindEven,listVal))
    print("Data after filter is : ",FData)

    MData=list(map(Squares,FData))
    print("Data after using map is : ",MData)

    RData=reduce(ProductOfAll,MData)
    print("Output of Reduce  : ",RData)

if __name__=="__main__":
    main()