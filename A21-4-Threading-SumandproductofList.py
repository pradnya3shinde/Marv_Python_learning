import threading

sum_result = 0
product_result = 1

def calculate_sum(num_list):
    global sum_result
    for num in num_list:
        sum_result += num
     

# Function to calculate product of elements
def calculate_product(num_list):
    global product_result
    product = 1
    for num in num_list:
        product *= num
    product_result=product

def main():
    int_list = [10,4,6,78,9,3,2]
    
    thread1 = threading.Thread(target=calculate_sum, args=(int_list,))
    thread2 = threading.Thread(target=calculate_product, args=(int_list,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print(f"Sum of elements: {sum_result}")
    print(f"Product of elements: {product_result}")

if __name__ == "__main__":
    main()
