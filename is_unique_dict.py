## THIS IMPLEMENTATION RUNS IN O(N) and USES DICTIONARY FOR LOOKUP


def is_unique(string):
    LIST = list(string)
    LEN = len(LIST)
    Dict = {}
    for i in range(0,LEN):
        CHAR_ONE = LIST[i]
        Dict[CHAR_ONE] = 0
    for i in range(0,LEN):
        CHAR_ONE = LIST[i]
        Dict[CHAR_ONE] = Dict[CHAR_ONE] + 1
    del Dict[' ']
    NEW_LIST = Dict.values()
    NEW_LIST = list(NEW_LIST)
    for i in range (0, len(NEW_LIST)):
        NUMBER = NEW_LIST[i]
        if (NUMBER > 1):
            return (False)
    return (True)
    

    

if __name__ == "__main__":

    INPUT = input() #Give a string input to check if it has unique characters
    ANSWER = is_unique(INPUT)
    print (ANSWER)
    
    
