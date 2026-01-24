def TableOfNum(no):
    for i in range(1,11):
        print(no * i)
    
def main():
    no=int(input("Enter number: "))
    TableOfNum(no)

if __name__ =="__main__": 
    main()   