e7.txt
#7 DIT FFT
import numpy as np

#bit reversal
xn = [1,2,3,4,4,3,2,1]
index=[0,4,2,6,1,5,3,7]
x1=[xn[i] for i in index]
print(xn)
N=len(xn)

#2 point dft
y1=np.zeros(N)
N1=2
i=0
for j in range(N//N1):
        y1[i]=((x1[i]+x1[i+1]))
        y1[i+1]=((x1[i]-x1[i+1]))
        i+=N1
print("y1:",y1)

#4 point dft
y2=np.zeros(N,dtype=complex)
N1=4
i=0
for j in range(N//N1):
    y2[i]=((y1[i]+y1[i+2]))
    y2[i+1]=((y1[i+1]-1j*y1[i+3]))
    y2[i+2]=((y1[i]-y1[i+2]))
    y2[i+3]=((y1[i+1]+1j*y1[i+3]))
    i+=N1
print("y2:",y2.tolist())

y3=np.zeros(N,dtype=complex)
N1=8
i=0
for j in range(N//2):
    W8=np.exp(-2j*np.pi*j/N)
    y3[j]=y2[j]+y2[j+4]*W8
    y3[j+4]=y2[j]-y2[j+4]*W8
y3=np.round(y3,3)
y3=y3.tolist()
print("y",y3)
