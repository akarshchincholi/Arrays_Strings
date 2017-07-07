## THIS SOLUTON USES SORTING AND IS DONE IN O(N log N)


def check_permutation (str1, str2):
    LIST1 = list(str1)
    LIST2 = list(str2)
    LIST1.sort()
    LIST2.sort()
    str1 = ''.join(LIST1)
    str2 = ''.join(LIST2)
    if (str1 == str2):
        return (True)
    return (False)


if __name__ == "__main__":

    INPUT1 = input() #Give two strings as inputs to check for permutation
    INPUT2 = input()
    ANSWER = check_permutation(INPUT1,INPUT2)
    print (ANSWER)
