def Factorial(number):
    fact=1
    for i in range(1,number+1):
        fact=fact*i
    return fact

def main():
    value=int(input("Enter number: "))
    ret =Factorial(value)
    print("Factorial is: ",ret)


if __name__=="__main__":
    main()