#my solution 
def rotate(matrix):
    x = 0
    y = 0
    newmatrix = []
    newlist = []
    while x < len(matrix):
        while y < len(matrix[x]):
            newlist.append(matrix[y][x])
            y = y + 1
        x = x + 1
        y = 0
        newmatrix.append(newlist[::-1])
        newlist = []
        
            
        
    return newmatrix

# in place solution found from the web
def rotate90Clockwise(A): 
    N = len(A[0]) 
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            temp = A[i][j] 
            A[i][j] = A[N - 1 - j][i] 
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j] 
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
            A[j][N - 1 - i] = temp
    return A
print(rotate90Clockwise([[1,2,3],[4,5,6],[7,8,9]]))
