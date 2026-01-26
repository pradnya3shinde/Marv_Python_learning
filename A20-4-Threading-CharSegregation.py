import threading
   
def smallLetters(str):
    small_letters = [] 
    for char in str:
        if char.islower():
            small_letters.append(char)    
    print(f"Small letters: {''.join(small_letters)}")
    print(f"Thread id: {threading.get_ident()} Thread name: {threading.current_thread().name}")


def capitalLetters(str):
    capital_letters=[]
    for char in str:
        if char.isupper():
            capital_letters.append(char)
    print(f"Capital letters: {''.join(capital_letters)}")
    print(f"Thread id: {threading.get_ident()} Thread name: {threading.current_thread().name}")

def digits(str):
    digitsval=[]
    for char in str:
        if char.isdigit():
            digitsval.append(char)
    print(f"Digits are: {''.join(digitsval)}") 
    print(f"Thread id: {threading.get_ident()} Thread name: {threading.current_thread().name}")


def main():
    str="Marvellous25"
    small = threading.Thread(target=smallLetters,args=(str,))
    capital = threading.Thread(target=capitalLetters,args=(str,))
    digit = threading.Thread(target=digits,args=(str,))

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()
    
    
if __name__=="__main__":
    main()

