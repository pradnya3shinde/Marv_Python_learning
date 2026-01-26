def Printpattern(cnt):
    for i in range(cnt):
        for j in range(1,cnt+1):
            print(j,end=" ") 
        print()

def main():
    Printpattern(5)


if __name__=="__main__":
    main()  