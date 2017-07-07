# Zero Matrix done in 0(N^2)
from numpy import matrix
def zero_matrx(MATRIX):
    Rows = []
    Columns = []
    N = len(MATRIX)
    for i in range (0,N):
        for j in range (0,N):
            if (MATRIX[i][j] == 0 ):
                Rows.append(i)
                Columns.append(j)
    Rows = set(Rows)
    Rows = list(Rows)
    #print (Rows)
    Columns = set(Columns)
    Columns = list(Columns)
    #print (Columns)
    for i in range (0,N):
        if (i in Rows):
            for j in range(0,N):
                MATRIX[i][j] = 0
        if (i in Columns):
            for j in range(0,N):
                MATRIX[j][i] = 0
    return (MATRIX)
    
    
if __name__ == "__main__":
    Order = input()                 #Give the order of the matrix to make it NxN
    Order = int(Order)
    M = []
    for i in range(0,Order):        
        INPUT = input()   # Give rows as inputs
        LIST = list(map(int, INPUT.split(' ')))
        M.append(LIST)
    N = matrix(M)
    print (N)                   # Original Matrix
    ANSWER = zero_matrx(M)
    ANSWER = matrix(ANSWER)
    print (ANSWER)              # Zero MAtrix
        
