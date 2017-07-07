## WE DO THIS BY COUNTING OCCURENCES and
## MAKING SURE THEY ARE EVEN AND AT MAX ONE CAN HAVE ODD
## ALSO USE DICTIONARY IN O(N) TIME.

def Palindrome_Permutation(STRING):
    DICT = {}
    for i in range (0, len(STRING)):
        ELEMENT = STRING[i]
        ELEMENT = ELEMENT.lower()
        DICT[ELEMENT] = 0
    for i in range (0, len(STRING)):
        
        
        ELEMENT = STRING[i]
        ELEMENT = ELEMENT.lower()
        DICT[ELEMENT] += 1
    del DICT[' '] # Handle the case where ' ' does not exist
    VALUES = list(DICT.values())
    Count = 0
    for i in range(0, len(VALUES)):
        NUMBER = VALUES[i]
        if ((NUMBER % 2) != 0):
            Count += 1
            if (Count > 1):
                return (False)
    return (True)


if __name__ == '__main__':
    INPUT = input() # Give an input to test for palindrome test
    ANSWER = Palindrome_Permutation(INPUT)
    print (ANSWER)
    
        
