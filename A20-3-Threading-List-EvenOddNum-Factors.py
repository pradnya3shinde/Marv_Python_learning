import threading
   
def even_factors_sum(lst):
    total_sum = 0
    for i in lst:
        if i % 2 == 0: 
            total_sum += i
    print("Even Sum: ",total_sum)

def odd_factors_sum(lst):
    total_sum = 0
    for i in lst:
        if i % 2 == 1: 
            total_sum += i
    print("Odd Sum: ",total_sum)


def main():
    lst=[10,20,30,5,7,12]
    even_thread = threading.Thread(target=even_factors_sum,args=(lst,))
    odd_thread = threading.Thread(target=odd_factors_sum,args=(lst,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()
    
    print("Exis from main")
    
if __name__=="__main__":
    main()

