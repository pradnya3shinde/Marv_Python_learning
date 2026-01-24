
def PrintReverseNNumbers(no):
    for i in range(no,0,-1):
        print(i)
         

def main():
    no = int(input("Enter a number: "))
    print("Numbers in reverse order till given number:")
    PrintReverseNNumbers(no)
    

if __name__=="__main__":
    main