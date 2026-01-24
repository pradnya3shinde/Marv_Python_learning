 
def PrintEvenNum(number):
    for i in range(1, number + 1):
        if i % 2 == 0:
            print(i)

def main():
    no=int(input("Enter number: "))
    print("Even numbers till given number:")
    PrintEvenNum(no)
    


if __name__=="__main__":
    main()