import sys

def IsExistsWord(filename,word):
    count = 0
    file= open(filename, "r")
    for line in file:
        words = line.split()
        count += words.count(word)

    if(count>1):
        print(f"Found word {word} {count} times",)
    else:
        print(f"Word {word} not found")    

def main():
    if len(sys.argv) != 3:
        print("invalid Args.")
        return

    file = sys.argv[1]    
    word = sys.argv[2]    
    IsExistsWord(file,word)
    
if __name__=="__main__":
    main()  

   
