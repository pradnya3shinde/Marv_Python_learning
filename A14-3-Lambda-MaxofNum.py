# syntas lambda parameters: function body
Maximum= lambda no1,no2: no1 if no1>no2 else no2   

def main():
    no1=int(input("Enter number: "))
    no2=int(input("Enter number: "))
    ret =Maximum(no1,no2)
    print("Maximum Number is: ",ret)


if __name__=="__main__":
    main()