import numpy as np
import cv2
import matplotlib.pyplot as plt

a=cv2.imread('man_ref.png')
plt.imshow(a)
plt.show()

import cv2
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
a1=cv2.imread("pos_img1/1.png")
a2=cv2.imread("neg_img1/1.png")
plt.imshow(a2)
plt.show()

topleft = np.array([565, 352])
bottomright = np.array([992, 780])
total_proj_pixel = 16

H = np.array([[1]])
for i in range(0, 4):
    H = np.vstack((np.hstack((H, H)), np.hstack((H, -H))))
image_dimension_crop = abs(bottomright - topleft + 1)
total_image_pixel_crop = np.array((image_dimension_crop))
print(H)


#reshaping the images so that the cropped image encompasses correctly the hadamard code that is projected
filepath=glob.glob('car_pos_img/*.png')
for f in filepath:
    x=cv2.imread(f)
    print(f)
    #x=x[topleft[0]:topleft[0]+430,topleft[1]:topleft[1]+430]
    x = x[352:780,565:992]
    cv2.imwrite(f,x)

filepath=glob.glob('car_neg_img/*.png')
for f in filepath:
    x=cv2.imread(f)
    print(f)
    #x=x[topleft[0]:topleft[0]+430,topleft[1]:topleft[1]+430]
    x = x[352:780,565:992]
    cv2.imwrite(f,x)


#Reshaping each channel of the captured image which is of size(m,n,3) to a vector of size (mn,1)
lpos1 = []
lpos2 = []
lpos3 = []
npos1 = []
npos2 = []
npos3 = []
filepath = glob.glob('car_pos_img/*.png')
for f in filepath:
    x = cv2.imread(f)
    [m, n, p] = np.shape(x)
    x1 = np.reshape(x[:,:,0], (m * n, 1))
    x2 = np.reshape(x[:, :, 1], (m * n, 1))
    x3 = np.reshape(x[:, :, 2], (m * n, 1))
    lpos1.append(x1)
    lpos2.append(x2)
    lpos3.append(x3)
filepath = glob.glob('car_neg_img/*.png')
for f in filepath:
    x = cv2.imread(f)
    [m, n, p] = np.shape(x)
    x1 = np.reshape(x[:, :, 0], (m * n, 1))
    x2 = np.reshape(x[:, :, 1], (m * n, 1))
    x3 = np.reshape(x[:, :, 2], (m * n, 1))
    npos1.append(x1)
    npos2.append(x2)
    npos3.append(x3)
lpos1 = np.asarray(lpos1)
lpos2 = np.asarray(lpos2)
lpos3 = np.asarray(lpos3)

npos1 = np.array((npos1))
npos2 = np.array((npos2))
npos3 = np.array((npos3))
print(np.shape(lpos1),np.shape(npos1))
[bb,aa,cc]=np.shape(lpos1)

lpos1 = np.transpose(np.reshape(lpos1, (bb,aa)))
lpos2 = np.transpose(np.reshape(lpos2, (bb,aa)))
lpos3 = np.transpose(np.reshape(lpos3, (bb,aa)))

npos1 = np.transpose(np.reshape(npos1, (bb,aa)))
npos2 = np.transpose(np.reshape(npos2,(bb,aa)))
npos3 = np.transpose(np.reshape(npos3, (bb, aa)))

ll=np.empty((aa,bb,3),dtype=float)
ll[:,:,0]=lpos1
ll[:,:,1]=lpos2
ll[:,:,2]=lpos3

nn=np.empty((aa,bb,3))
nn[:,:,0]=npos1
nn[:,:,1]=npos2
nn[:,:,2]=npos3
c = ll-nn

print(np.shape(c))


Hpos = np.transpose(H);

for i in range(16):
    for j in range(16):
        if Hpos[i, j] < 0:
            Hpos[i, j] = 0

# print(Hpos)
T=np.empty((aa,bb,3))
T[:,:,0] = c[:,:,0] @ np.linalg.inv(np.transpose(Hpos))
T[:,:,1] = c[:,:,1] @ np.linalg.inv(np.transpose(Hpos))
T[:,:,2] = c[:,:,2] @ np.linalg.inv(np.transpose(Hpos))

print(np.shape(T))
np.save("Tmatrixman",T)

#Relighting part
x1=np.empty((aa,1,3))
x1[:,:,0] = T[:,:,0]@np.ones((16, 1))*0
print(x1[:,:,0])
x1[:,:,1] = T[:,:,1] @ np.ones((16, 1))*1
print(x1[:,:,1])
x1[:,:,2] = T[:,:,2] @ np.ones((16, 1))*0

x1 = np.reshape(x1, (428, 427,3))
for i in range(np.shape(x)[0]):
    for j in range(np.shape(x)[1]):
        for k in range(np.shape(x)[2]):
            if x[i, j,k] < 0:
                x[i, j,k] = 0
print(x1)
y=np.empty((428,427,3))
y[:,:,0]=x1[:,:,2]
y[:,:,1]=x1[:,:,1]
y[:,:,2]=x1[:,:,0]

cv2.imwrite("aquaman.png", y)

