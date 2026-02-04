import sys

def CountOccurences(filename,word):
    count = 0
    file= open(filename, "r")
    for line in file:
        words = line.split()
        count += words.count(word)

    print("Occurrences of", word, ":", count)

def main():
    if len(sys.argv) != 3:
        print("invalid Args.")
        return

    file = sys.argv[1]    
    word = sys.argv[2]    
    CountOccurences(file,word)
    
if __name__=="__main__":
    main()  

   
 



