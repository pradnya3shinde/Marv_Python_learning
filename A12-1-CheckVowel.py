def CheckVowel(char):
    if len(char) == 1 and char.isalpha():
        ch = char.lower()
    
        if ch in ['a', 'e', 'i', 'o', 'u']:
            print("Character is a vowel")
        else:
            print("Character is a consonant")
    else:
        print("Invalid input! ")

def main():
    char = input("Enter a single character: ")
    CheckVowel(char)
    

if __name__=="__main__":
    main()