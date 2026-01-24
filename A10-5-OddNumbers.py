 
def PrintOddNum(number):
    for i in range(1, number + 1):
        if i % 2 == 1:
            print(i)

def main():
    no=int(input("Enter number: "))
    print("Odd numbers till given number:")
    PrintOddNum(no)
    


if __name__=="__main__":
    main()