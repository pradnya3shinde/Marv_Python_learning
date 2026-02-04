import sys

def CountLines(filename):
    count = 0
    file= open(filename, "r")
    for line in file:        
        words = line.split()
        count += len(words)

    print("Total lines are", count)

def main():
    if len(sys.argv) != 2:
        print("invalid Args.")
        return

    file = sys.argv[1]    
    CountLines(file)
    
if __name__=="__main__":
    main()  
 



