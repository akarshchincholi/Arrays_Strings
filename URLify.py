## We replace ' ' with '%20' in O(N) time

def URLify(String):
    LIST = list(String)
    CHAR = '%20'
    for i in range (0, len(LIST)):
        ELEMENT = LIST[i]
        if (ELEMENT == ' '):
            LIST[i] = CHAR

    StringNEW = ''.join(LIST)
    return (StringNEW)


if __name__ == '__main__':
    INPUT = input() # Give an input with spaces in it to perform URLify
    ANSWER = URLify(INPUT)
    print (ANSWER)
        
        
