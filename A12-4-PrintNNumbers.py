
def PrintNNumbers(no):
    for i in range(1, no + 1):
        print(i)
         

def main():
    no = int(input("Enter a number: "))
    PrintNNumbers(no)
    

if __name__=="__main__":
    main()