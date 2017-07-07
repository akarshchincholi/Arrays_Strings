## THIS APPROACH USES SORTING and RUNS in O(N log N)


def one_away(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    LIST1 = list(str1)
    LIST2 = list(str2)
    LIST1.sort()
    LIST2.sort()
    print (LIST1)
    print (LIST2)
    if (len(LIST1) == len(LIST2)):

        Count = 0
        for i in range(0,len(LIST1)):
            if (LIST1[i] != LIST2[i]):
                Count += 1
        print (Count)
        if (Count > 1):
            return (False)
        return (True)

    L1 = len(LIST1)
    L2 = len(LIST2)

    if (L1 > L2):
        for i in range (0, L2):
            ELEMENT = LIST2[i]
            if (ELEMENT in LIST1):
                LIST1.remove(ELEMENT)
        print (LIST1)
        if (len(LIST1) == 1):
            return (True)
        else:
            return (False)

    if (L2 > L1):
        for i in range (0, L1):
            ELEMENT = LIST1[i]
            if (ELEMENT in LIST2):
                LIST2.remove(ELEMENT)
        print (LIST2)
        if (len(LIST2) == 1):
            return (True)
        else:
            return (False)


if __name__ == "__main__":
    IN1 = input()               # GIVE TWO STRING INPUTS TO CHECK IF THEY ARE ON CHARACTER AWAY
    IN2 = input()
    ANSWER = one_away(IN1,IN2)
    print (ANSWER)
