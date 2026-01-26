from functools import reduce

def AcceptNumbers(no):
    lst=[]
    for i in range(no):
        lst.append(int(input("Enter number:")))
    return lst

Squares = lambda no:(no*no) 
GreaterByNum=lambda no: no>=70 and no<=90
Increment=lambda no: no+10
ProductOfAll= lambda a,b : a*b

def main():
    n = int(input("Enter how many number you want to enter: "))
    listVal=AcceptNumbers(n)
    
    FData=list(filter(GreaterByNum,listVal))
    print("Data after filter is : ",FData)

    MData=list(map(Increment,FData))
    print("Data after using map is : ",MData)

    RData=reduce(ProductOfAll,MData)
    print("Output of Reduce  : ",RData)

if __name__=="__main__":
    main()