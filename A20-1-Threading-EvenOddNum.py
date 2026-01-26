import threading
   
def print_even():
    num = 0
    count = 0
    while count < 10:
        print(f"Even: {num}")
        num += 2   
        count += 1

def print_odd():
     num = 0
     count = 0
     while count < 10:
        print(f"Odd: {num}")
        num += 1   
        count += 1

def main():
    even_thread = threading.Thread(target=print_even)
    odd_thread = threading.Thread(target=print_odd)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()
    
if __name__=="__main__":
    main()

