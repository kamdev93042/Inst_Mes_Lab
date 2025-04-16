
#6 Overlap add method
import numpy as np

def c_conv(xn,hn):
  N = max(len(xn),len(hn))

  hn = np.pad(hn, (0,N-len(hn)), 'constant')
  xn = np.pad(xn, (0,N-len(xn)), 'constant')
  y = np.zeros(N)

  #performing Circular Convolution
  for n in range(N):
    for i in range(N):
      y[n] += xn[i]*hn[n-i] 
  return y


# main program
xn=[3,-1,0,1,3,2,0,1,2,1]
#xn=[1,2,3,3,2,1,-1,-2,-3,5,6,-1,2,0,2,1]
print(len(xn))
hn=[1,1,1]
#hn= [3,2,1,1]
xn=np.array(xn)
hn=np.array(hn)

N=len(xn)
M=len(hn)
#(block_length=M+L-1)
L=5

#total length of the output
y1 = np.zeros(N+M-1)

#number of blocks
n =  int(np.ceil(N/L))

for i in range(n):

    #slice the current block
    start = i*L
    end = min(start+L,N)
    x_block = xn[start:end]

    #pad if it's the last block
    if len(x_block)<L:
        x_block = np.pad(x_block,(0,L-len(x_block)),'constant')

    x_block = np.pad(x_block,(0,M-1),'constant')
    print("x_Block",x_block)


    #perform Circular convolution on the block
    y_block = c_conv(x_block,hn)
    print("y",y_block)
    print("y1",y1)
    print("Start, end",start,start+L+M-1)
    print("Y1_s",y1[start:start+L+M-1])
    y1[start:start+L+M-1] += y_block
    print("")

print("Y1",y1)
print(len(y1))
    
