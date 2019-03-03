seenx = []
seeny = []
def getzeros(matrix):
    points = []
    x= 0
    y = 0
    while x < len(matrix):
        while y < len( matrix[x]):
            if matrix[x][y] == 0:
                points.append((x,y))
            y = y + 1
        y = 0
        x = x + 1
    return points
def zeropoints(matrix,points):
    for point in points:
        matrix = zeropoint(matrix,point)
    return matrix
def zeropoint(matrix,point):
    matrix = zerorow(matrix,point[0])
    matrix = zerocolumn(matrix,point[1])
    
    return matrix
def zerorow(matrix,row):
    x = 0
    if row in seenx:
        return matrix
    while x  <  len(matrix[row]):
        matrix[row][x] = 0
        x = x + 1
    seenx.append(row)
        
    return matrix
def zerocolumn(matrix,column):
    y = 0
    if column in seeny:
        return matrix
    while y < len(matrix):
        matrix[y][column] = 0
        y = y+1
    seeny.append(column)
    return matrix
def zeromat(matrix):
    points = getzeros(matrix)
    print(matrix)
    return zeropoints(matrix,points)
print(zeromat([[0,1,1],[99,3,2]]))
