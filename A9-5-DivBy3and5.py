def DivBy3and5(no1):     
    if(no1%3==0 and no1%5==0):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")



def main():
    no1=int(input("Enter number: "))
    DivBy3and5(no1)  

if __name__ == "__main__":
    main()   