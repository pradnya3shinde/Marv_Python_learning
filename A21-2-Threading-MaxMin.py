import threading

def display_min(int_list):     
    temp=int_list[0]
    for num in int_list:
        if num < temp:
            temp=num
    print(f"Minimum number: {temp}")

def display_max(int_list):
    
    temp=int_list[0]
    for num in int_list:
        if num > temp:
           temp=num
    print(f"Maximum number: {temp}")

def main():
    int_list = [21, 17, 19, 20, 23, 45, 28, 29, 31, 33, 35]
    
    thread1 = threading.Thread(target=display_max, args=(int_list,))
    thread2 = threading.Thread(target=display_min, args=(int_list,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
