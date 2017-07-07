## THIS SOLUTION USED DICTIONARY AND RUNS IN O(N) TIME

def check_permutation(str1,str2):
    Dict1 = {}
    for i in range (0,len(str1)):
        CHAR = str1[i]
        Dict1[CHAR] = 0
    for i in range (0,len(str1)):
        CHAR = str1[i]
        Dict1[CHAR] = Dict1[CHAR] + 1
    Dict2 = {}
    for i in range (0,len(str2)):
        CHAR = str2[i]
        Dict2[CHAR] = 0
    for i in range (0,len(str2)):
        CHAR = str2[i]
        Dict2[CHAR] = Dict2[CHAR] + 1
    for key,value in Dict1.items():
        if (Dict2[key] != Dict1[key]):
            return (False)

    return(True)

if __name__ == "__main__":
    INPUT1 = input() #Give two strings as inputs to check for permutation
    INPUT2 = input()
    ANSWER = check_permutation(INPUT1,INPUT2)
    print (ANSWER)    
