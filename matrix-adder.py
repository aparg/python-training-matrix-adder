# ************************Matrix Addition**********************************


#Matrix addition function
def MatrixAdder(mat1,mat2):
    addedMatrix = [[0]*len(mat1[0]) for i in range(len(mat1))]
    for li_index,matEl in enumerate(mat1):
        for index,liEl in enumerate(matEl):
            addedMatrix[li_index][index] = mat1[li_index][index] + mat2[li_index][index]
    return addedMatrix

#Driver Code
print("Enter the dimension of matrices to be added")
row = int(input("Enter number of rows"))
col = int(input("Enter number of columns"))

#List initialization
mat_1 = [[0]*col for i in range(row)]
mat_2 = [[0]*col for i in range(row)]

# Input of matrix values
print("\nFor Matrix 1:")
for r in range(0,row):
    for c in range(0,col):
        mat_1[r][c] = int(input("Enter the value  at position ["+str(r)+"]"+"["+str(c)+"]\n"))

print("For Matrix 2:")
for r in range(0,row):
    for c in range(0,col):
        mat_2[r][c] = int(input("Enter the value  at position ["+str(r)+"]"+"["+str(c)+"]\n"))

#Function call and print 
print("******************************************OUTPUT**********************************************************************")
print("The sum of "+str(mat_1)+" and "+str(mat_2)+"is:")
print(MatrixAdder(mat_1,mat_2))
print("**********************************************************************************************************************")