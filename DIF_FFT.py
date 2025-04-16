
#WAP to perform radix 2 DIF FFT of a sequence x(n)={1,2,3,3,2,1,0,1}
import numpy as np
xn = [1,2,3,3,2,1,0,1]
print("xn: ",xn)

# 8-point FFT
N=8
y1=np.zeros(8,dtype=complex)
for j in range(N//2):
  W8 = np.exp((-1j * 2 * np.pi * j / N))
  y1[j]=np.round((xn[j]+xn[j+4]),3)
  y1[j+4]=np.round((xn[j]-xn[j+4])*W8,3)

# Convert elements in y1 to standard Python types
y1 = [complex(round(x.real, 3), round(x.imag, 3)) if isinstance(x, np.complex128) else int(x) if isinstance(x, np.int64) else x for x in y1]
print("\ny1: ",y1)

# 4-point FFT
y2=[]
for j in range(8):
  if j in [0,1,4,5]:
    y2.append((y1[j]+y1[j+2]))  #W4[0] = 1
  else:
    y2.append((y1[j-2]-y1[j]))  #W4[0] =-1
print("y2: ",y2)

# Multiplying with WN2
y2[3]=y2[3]*(-1j)
y2[7]=y2[7]*(-1j)
#print("updated y2 after multiplication: \n",y2)

# 2-point FFT
y3 = []
for j in range(8):
  if j%2==0:
    y3.append((y2[j]+y2[j+1]))  #W2[0] = 1
  else:
    y3.append((y2[j-1]-y2[j]))  #W2[1] =-1
y3=[round(x.real,3)+round(x.imag,3)*1j if isinstance(x,complex) else round(x,3) for x in y3]
print("y3: ",y3)

#bit reversal
def bit_reversal(n, bits):
    return int(bin(n)[2:].zfill(bits)[::-1], 2)


updated_index=[]
# 3-bit reversal:
for i in range(8):  # Numbers from 0 to 7 (3 bits)
    reversed_i = bit_reversal(i, 3)
    updated_index.append(reversed_i)
#print("\nUpdated_Index: ",updated_index)


y=[]
for i in updated_index:
  y.append(y3[i])
  j=+1

print("\nTruncated Y after bit rev:")
y = [round(x.real, 3) + round(x.imag, 3) * 1j if isinstance(x, complex) else round(x, 3) for x in y]
print("Y: ",y)
