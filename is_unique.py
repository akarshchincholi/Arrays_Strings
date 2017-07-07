## THIS IMPLEMENTATION RUNS IN O(N ^ 2)


def is_unique(string):
    LIST = list(string)
    LEN = len(LIST)
    for i in range(0,LEN-1):
        CHAR_ONE = LIST[i]
        if (CHAR_ONE == ' '):
            continue
        for j in range(i+1, LEN):
            CHAR_TWO = LIST[j]
            if (CHAR_ONE == CHAR_TWO):
                return (False)
    return (True)

if __name__ == "__main__":

    INPUT = input() #Give a string input to check if it has unique characters
    ANSWER = is_unique(INPUT)
    print (ANSWER)
    
    
