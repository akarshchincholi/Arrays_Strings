## Dictionary To Count Chracter Occurences O(N)

def string_compression(STRING):
    LIST = list(STRING)
    DICT = {}
    for i in range (0,len(STRING)):
        ELEMENT = LIST[i]
        DICT[ELEMENT] = 0
    for i in range (0,len(STRING)):
        ELEMENT = LIST[i]
        DICT[ELEMENT] += 1

    NEW = ''

    print (DICT)
    for key,value in DICT.items():
        
        TEMP = key+str(value)
        #print(TEMP)
        NEW = NEW + TEMP
    return(NEW)

if __name__ == "__main__":
    STR = input()
    ANSWER = string_compression(STR)
    if (len(ANSWER) < len(STR)):
        print (ANSWER)
    else:
        print (STR)
        
    
    
