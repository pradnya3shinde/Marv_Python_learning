def FindFrequencyofElemnt(no):
    lst=[]
    for i in range(no):
        lst.append(int(input("Enter number:")))

    findN=int(input("Enter element to search: ")) 
    count=0   

    min=lst[0]    
    for j in lst:
         if j ==findN:
            count+=1

    print("Frequency of given number is: ",count)    


def main():
    n = int(input("Enter how many number you want to enter: "))
    FindFrequencyofElemnt(n)
    

if __name__=="__main__":
    main()