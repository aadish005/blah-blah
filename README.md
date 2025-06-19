mport numpy as np

order = int(input("Enter the order (2 or 3): "))

matrix = []
print("Enter the matrix row by row:")
for i in range(order):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    matrix.append(row)

vector = []
print("Enter the vector values:")
for i in range(order):
    val = float(input(f"b{i+1}: "))
    vector.append(val)

A = np.array(matrix)
b = np.array(vector)

print("\nMatrix A:")
print(A)

print("\nVector b:")
print(b)
