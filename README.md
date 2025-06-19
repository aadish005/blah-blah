import numpy as npy
import scipy.linalg as lu
order=input("Enter the order of the matrix.\t")
r,c=map(int,order.lower().split('x'))
matrix=[]
for i in range(r):
    row=[]
    for j in range(c):
        temp=int(input(f"Enter the element in {i+1}th row"))
        row.append(temp)
    matrix.append(row)
matrix=npy.array(matrix)    
print(matrix)
P,L,U = lu.lu(matrix)
print("After LU decompostion......\n")
print("Permutated state:\n")
print(P)
print("Lower triangular state:\n")
print(L)
print("Upper triangular state:\n")
print(U)        
