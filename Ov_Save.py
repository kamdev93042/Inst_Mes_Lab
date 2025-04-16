
#5 Overlap save method
import numpy as np
def c_conv(xn,hn,x1,yn1):
  M = len(hn)
  N = len(xn)

  # padding
  if M<N:
    hn = np.pad(hn, (0,N-M), 'constant', constant_values=0)
  else:
    xn = np.pad(xn, (0,M-N), 'constant', constant_values=0)
  yn = []

  #performing Circular Convolution
  for x in range(N):
    y=0
    for i in range(N):
      y = y+ xn[i]*hn[x-i]
    yn=np.append(yn,y)
  print(f"Y{x1}: {yn}")

#discarding M-1 Samples
  yn1.extend(yn[M-1:])
  return yn1



##############################
# main program start here
##############################
hn=[1,1,1]
hn=np.array(hn)
M=len(hn)

xn=[3,-1,0,1,3,2,0,1,2,1]
xn=np.array(xn)
N=len(xn)
L= int(input("Enter section length (L):"))
#L>M, use L=4

yn1=[]  #final matrix

# dividing into blocks
i=0
#numbering of blocks
x1=1
while i<N:
  if i<L:
    xn1=xn[i:i+L]
    xn1=np.pad(xn1, (M-1, 0), 'constant', constant_values=0)
    print(f"X{x1}:{xn1}")
    c_conv(xn1,hn,x1,yn1)
    x1+=1
  else:
    if i+L<=N:
       xn2=xn[i-M+1:i+L]
       print(f"X{x1}:{xn2}")
       c_conv(xn2,hn,x1,yn1)
       x1+=1

    if i+L>N:
      xn3=xn[i-M+1:N]
      xn3=np.pad(xn3, (0, i+L-N), 'constant', constant_values=0)
      print(f"X{x1}:{xn3}")
      c_conv(xn3,hn,x1,yn1)
      x1+=1
  i=i+L

print(f"Y:{yn1}")  #final Matrix



# Checking the matrix using Linear Convolution


