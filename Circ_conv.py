import numpy as np

def circular_convolution(xn, hn):
    N = max(len(xn), len(hn))
    
    # Append zeros to make lengths equal
    xn = np.array(xn + [0] * (N - len(xn)))
    hn = np.array(hn + [0] * (N - len(hn)))

    # Compute circular convolution
    yn = []
    for n in range(N):
        val = 0
        for k in range(N):
            val += xn[k] * hn[(n - k) % N]  # Circular indexing
        yn.append(val)

    return yn

# Given sequences
xn = [1, -1, -2, 3, -1]
hn = [1, 2, 3]

# Perform circular convolution
result = circular_convolution(xn, hn)

# Output
print("Circular Convolution Result:", result)
