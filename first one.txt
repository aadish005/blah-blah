import numpy as np

order = input("Enter the order of the matrix (e.g., 3x3): ")
r, c = map(int, order.lower().split('x'))

a = []
for i in range(r):
    row = []
    for j in range(c):
        temp = int(input(f"Enter element at ({i}, {j}): "))
        row.append(temp)
    a.append(row)

a = np.array(a)
print("Matrix:")
print(a)
