import threading
   
def even_factors_sum(no):
    total_sum = 0
    for i in range(1, no+1):
        if no % i == 0 and i % 2 == 0: 
            total_sum += i
    print("Even Sum: ",total_sum)

def odd_factors_sum(no):
    total_sum = 0
    for i in range(1, no+1):
        if no % i == 0 and i % 2 == 1: 
            total_sum += i
    print("Odd Sum: ",total_sum)


def main():
    no = int(input("Enter a number: "))
    even_thread = threading.Thread(target=even_factors_sum,args=(no,))
    odd_thread = threading.Thread(target=odd_factors_sum,args=(no,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()
    
    print("Exis from main")
    
if __name__=="__main__":
    main()

