from functools import reduce

def AcceptNumbers(no):
    lst=[]
    for i in range(no):
        lst.append(int(input("Enter number:")))
    return lst

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

MultBy2= lambda a : a*2
MaxVal= lambda a,b: a if a>b else b

def main():
    n = int(input("Enter how many number you want to enter: "))
    listVal=AcceptNumbers(n)
    
    FData=list(filter(isPrime,listVal))
    print("Data after filter is : ",FData)

    MData=list(map(MultBy2,FData))
    print("Data after using map is : ",MData)

    RData=reduce(MaxVal,MData)
    print("Output of Reduce  : ",RData)

if __name__=="__main__":
    main()