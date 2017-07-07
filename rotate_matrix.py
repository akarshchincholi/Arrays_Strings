# Rotate an NxN Matrix clockwise by 90 degrees by observing the pattern
from numpy import matrix

def rotate_matrix(MATRIX):
    N = len(MATRIX)    
    NEW = []
    for i in range (0,N):
        LIST = []
        for j in range (0,N):
            LIST.append(0)
        NEW.append(LIST)
    for i in range(0,N):
        for j in range(0,N):
            NEW[i][j] = MATRIX[N-1-j][i]
    return (NEW)

if __name__ == "__main__":
    Order = input()            # Give the order N so that we can take NxN matrix as input
    Order = int(Order)
    MATRIX = []    
    for i in range (0,Order):
        INPUT = input()     # give each row as input where elements are separated by ' ' i.e. space
        LIST = INPUT.split(' ')
        MATRIX.append(LIST) 
    ANSWER = rotate_matrix(MATRIX)
    MAT = matrix(MATRIX)
    ANSWER = matrix(ANSWER)
    print (MAT)
    print (ANSWER)

            
            
