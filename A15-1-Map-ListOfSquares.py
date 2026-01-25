from functools import reduce


Squares = lambda no:(no*no) 

def main():
    data=[11,10,15,20,22,27,30]
    print("Actual Data is: ",data)

    MData=list(map(Squares,data))
    print("Data after increment using map is : ",MData)
 

if __name__=="__main__":
    main()