def SumOfNaturalNum(no):
    total = 0
    for i in range(1, no + 1):
        total += i
    print("Sum of natural numbers: ",total)

def main():
    no=int(input("Enter number: "))
    SumOfNaturalNum(no)

if __name__ =="__main__": 
    main()   

   