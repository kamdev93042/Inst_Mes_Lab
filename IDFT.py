
#4: IDFT

import numpy as np
import matplotlib.pyplot as plt
import cmath
X = [5, 0, 1-1j, 0, 1, 0, 1+1j, 0]
N = len(X)
print("No. of elements:",N)
print("Given Series, ")
print(X)
R = N//2

# Initialize W matrix
W = np.zeros((N, N), dtype=complex)

for k in range(R):
  W[1,k] = cmath.exp(-2j * np.pi * 1 * k / 8)

for i in range(R):
  # for n in range(N):
    for k in range(N):
        if k%R == i:
          if k>3:
            W[1,k] = -W[1,i]


for i in range(N):
  for n in range(N):
    for k in range(N):
        if n*k%N == i:
            W[n,k] = W[1,i]


W = np.round(W,3)
print(N,"-Points DFT Twiddle Factor Matrix ,")
print(W)

W_inv = np.conjugate(W)
DFT_INV = (1/N)*np.matmul(W_inv,X)
DFT_INV = np.round(DFT_INV,3)
print("IDFT Result,")
for i in range(N):
  print(DFT_INV[i], end =",")
