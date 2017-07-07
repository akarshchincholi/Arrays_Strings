## THIS APPROACH USES OCCURENCE COUNTING AND RUNS IN O(N)

def one_away(str1, str2):
    DICT1 = {}
    LIST1 = list(str1)
    for i in range (0,len(LIST1)):
        ELEMENT = LIST1[i]
        DICT1[ELEMENT] = 0
    for i in range (0,len(LIST1)):
        ELEMENT = LIST1[i]
        DICT1[ELEMENT] += 1
    DICT2 = {}
    LIST2 = list(str2)
    for i in range (0,len(LIST2)):
        ELEMENT = LIST2[i]
        DICT2[ELEMENT] = 0
    for i in range (0,len(LIST2)):
        ELEMENT = LIST2[i]
        DICT2[ELEMENT] += 1
    MISMATCH = 0
    for key,value in DICT1.items():
        ONE = DICT1[key]
        TWO = 0
        if key in DICT2:
            TWO = DICT2[key]        
        if (ONE != TWO):
            MISMATCH += 1
            if (abs(ONE - TWO) > 1):
                return (False)
            if (MISMATCH > 1):
                return (False)
    return (True)


if __name__ == "__main__":
    IN1 = input()               # GIVE TWO STRINGS TO CHECK IF THEY ARE ONE CHAR AWAY
    IN2 = input()
    ANSWER = one_away(IN1,IN2)
    print (ANSWER)
        
        
        
