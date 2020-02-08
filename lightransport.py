'''
If size of a projection is pxq
With one pixel turned on at a time capture pq number of images
Suppose camera resolution is mxn
Reshape it to (mn,1) and stack all the images columnwise corresponding to the number of illumination patterns
This gives light transport matrix T of size (mnxpq)

'''
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
T=[]
cnt=0
[w,h]=[1600,1200]
for filename in os.listdir("capture_pos2"):
    img=cv2.imread("capture_pos2/"+filename,0)
    [w,h]=np.shape(img)
    img=np.reshape(img,(w*h,1))
    T.append(img)
    cnt=cnt+1


T=np.transpose(T)
T=np.reshape(T,(w*h,cnt))
#plt.imshow(T)
#plt.show()

'''
Relighting Code
T matrix(mnxpq)
Multiply by the projector lighting that is desired (pqx1)
In the column pq set the values of color and the corresponding pixel that has to be illuminated

'''

mask=np.zeros((16,16))
for i in range(16):
    for j in range(16):
        if i%10==0:
            mask[i,j]=255
cv2.imwrite("img.png",mask)
mask=np.reshape(mask,(256,1))
c=np.matmul(T,mask)
c=c.reshape((1200,1600))
print(c)
cv2.imwrite("relit.png",c)

