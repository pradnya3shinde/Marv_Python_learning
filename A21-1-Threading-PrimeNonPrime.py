import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def display_primes(int_list):
    primes = []
    for num in int_list:
        if is_prime(num):
            primes.append(num)
    print(f"Prime numbers: {primes}")

def display_non_primes(int_list):
    non_primes = []
    for num in int_list:
        if not is_prime(num):
            non_primes.append(num)
    print(f"Non Prime numbers: {non_primes}")

def main():
    int_list = [12, 17, 19, 20, 23, 25, 28, 29, 31, 33, 35]
    
    thread1 = threading.Thread(target=display_primes, args=(int_list,))
    thread2 = threading.Thread(target=display_non_primes, args=(int_list,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
