import numpy as np
import matplotlib.pyplot as plt
import cmath

x_n = []

N = int(input("Enter the number of elements: "))
for i in range(N):
    element = float(input(f"Enter element {i + 1}: "))
    x_n.append(element)

X_n = np.array([x_n])
x_n = X_n.T

print("No. of elements:", N)
print("Given Series, ")
print(X_n)

R = N // 2

# Initialize W matrix
W = np.zeros((N, N), dtype=complex)

for n in range(R):
    for k in range(R):
        W[n, k] = cmath.exp(-2j * np.pi * n * k / 8)

for i in range(R):
    for n in range(N):
        for k in range(N):
            if n * k % R == i:
                if (n * k // R) % 2 == 0:
                    W[n, k] = W[1, i]
                else:
                    W[n, k] = -W[1, i]

W = np.round(W, 3)
print(N, "-Points DFT Twiddle Factor Matrix .")
print(W)


DFT =np.matmul(W,X_n)
DFT = np.round(DFT, 3)
print("DFT Result, ")
print(DFT)





