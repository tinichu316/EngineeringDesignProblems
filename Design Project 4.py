#Solve a system of equations, first for a 3 variable, 3 equations system. It should indicate whether the solution is unique if it exists.

#store the coefficients in an augmented matrix Ax = b

Q = [
    [1, 0, 2, 9],
    [0, 1, 0, 5],
    [1, 1, 5, 9]
    ]

def getCoefficients(n):
    """Prompts the user for the coefficients to a nxn A matrix."""
    A = [0]*(n)
    for row in range(n):
        A[row] = [0]*(n+1)
    #ask for input
    for row in range(n):
        for col in range(n+1):
            A[row][col] = int(input("What is the coefficient in equation {}, column {}? ".format(row + 1, col + 1)))
    #prints out augmented matrix
    print("The inputted augmented matrix is:")
    for row in A:
        print(row)
    return A

def stairCase(A):
    emptyCols = []
    for currentCol in range(len(A)):
        for i in range(len(A)-1,-1,-1):
            if A[i][currentCol] == 0 and A[i][:currentCol] == [0]*len(A[i][:currentCol]):
                #move to the last row
                A.append(A[i])
                del A[i]
        if all(A[i][currentCol] == 0 for i in range(len(A))):
            emptyCols.append(currentCol)
    return A, emptyCols
            
        

def rowReduce(A):
    #this might be an error if the staircased matrix has a 1 in the 2nd col of the first row.
    A, emptyCols = stairCase(A)
    currentCol = 0
    currentRow = 0
    while currentCol < len(A):
        if currentCol not in emptyCols: #if we need to reduce this row
            #currentRow = 0
            if A[currentRow][currentCol] != 0:
                divisor = A[currentRow][currentCol]
                #the column is non empty,
                #divide the first row to have a leading 1
                for i in range(len(A[currentRow])):               
                    A[currentRow][i] /= divisor
                    
            #print("After creating a leading 1 in row {}, column {}, the matrix is :".format(currentRow + 1, currentCol + 1), Q)
            #clear the rest of the columns
            for row in range(currentRow + 1, len(A)):                
                if A[row][currentCol] != 0:
                    #subtract the first row
                    mult = A[row][currentCol]
                    for i in range(len(A[row])):
                        A[row][i] -= (A[currentRow][i] * mult) 
            currentCol += 1
            currentRow += 1
        else:
            currentCol += 1
        #print("Next iteration: ", Q)
    return A
        

a = [[0, -3, -6]]
#rowReduce(a)

#rowReduce(getCoefficients(2))    