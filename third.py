from scipy.linalg import lu_solve, lu_factor, inv, det

print("Enter the coefficients of the first equation:")
a1 = int(input("a1:\t"))
b1 = int(input("b1:\t"))
c1 = int(input("c1:\t"))

print("Enter the coefficients of the second equation:")
a2 = int(input("a2:\t"))
b2 = int(input("b2:\t"))
c2 = int(input("c2:\t"))

A = [[a1, b1], [a2, b2]]
B = [[c1], [c2]]

LU, piv = lu_factor(A)
x_gauss = lu_solve((LU, piv), B)

print("\nSolution using Gaussian Elimination:")
print(f"x = {x_gauss[0][0]}, y = {x_gauss[1][0]}")

if det(A) != 0:
    A_inv = inv(A)
    x_inverse = [
        [A_inv[0][0] * B[0][0] + A_inv[0][1] * B[1][0]],
        [A_inv[1][0] * B[0][0] + A_inv[1][1] * B[1][0]]
    ]
    print("\nSolution using Inverse Matrix Method:")
    print(f"x = {x_inverse[0][0]}, y = {x_inverse[1][0]}")
else:
    print("\nInverse Matrix Method not possible: matrix is singular (det =
