
import numpy as np

def manual_convolution(x, h, origin_x, origin_h):
    len_x = len(x)
    len_h = len(h)
    y = np.zeros(len_x + len_h - 1)

    for i in range(len_x):
        for j in range(len_h):
            y[i + j] += x[i] * h[j]

    origin_y = origin_x + origin_h
    return y, origin_y

# Get sequences from user
x = list(map(float, input("Enter the first sequence: ").split(',')))
h = list(map(float, input("Enter the second sequence: ").split(',')))

# Get origins from user
origin_x = int(input("Enter the origin position for the first sequence: "))
origin_h = int(input("Enter the origin position for the second sequence: "))

# Calculate lengths of the sequences
len_x = len(x)
len_h = len(h)

# Perform linear convolution using numpy
conv_np = np.convolve(x, h)
origin_np = origin_x + origin_h

# Perform manual convolution
conv_manual, origin_manual = manual_convolution(x, h, origin_x, origin_h)

# Calculate the length of the output sequence
len_output = len(conv_np)

# Find the sample position range
sample_position_range = (0, len_output - 1)

print("\nFirst sequence (x):", x)
print("Second sequence (h):", h)
print("Length of first sequence:", len_x)
print("Length of second sequence:", len_h)
print("Origin of first sequence:", origin_x)
print("Origin of second sequence:", origin_h)
print("\nLinear Convolution using numpy:", conv_np)
print("Origin of convolution (numpy method):", origin_np)
print("Linear Convolution using manual method:", conv_manual)
print("Origin of convolution (manual method):", origin_manual)
print("\nLength of the output sequence:", len_output)
print("Sample position range of the output sequence:", sample_position_range)

