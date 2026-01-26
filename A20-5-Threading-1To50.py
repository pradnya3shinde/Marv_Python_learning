import threading
   
def display_numbers_1_to_50():
    for i in range(1, 51):
        print(f"Thread 1: {i}")

def display_numbers_50_to_1():
    for i in range(50, 0, -1):
        print(f"Thread 2: {i}")

def main():
    t1 = threading.Thread(target=display_numbers_1_to_50,name="T1")
    t2 = threading.Thread(target=display_numbers_50_to_1,name="T2")

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    
    
if __name__=="__main__":
    main()

