import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (8.0, 8.0)

n = 8

# 8x8 source image
img_A = np.array([
        [255,     255,      255,      255,      255,      255,      255,      255],
        [255,     255,      255,        0,      0,        255,      255,      255],
        [255,     255,        0,        0,      0,          0,      255,      255],
        [255,       0,        0,        0,      0,          0,      0,        255],
        [255,     255,        0,        0,      0,          0,      255,      255],
        [255,     255,      255,        0,      255,      255,      255,      255],
        [255,     255,      255,      255,      255,      255,      255,      255],
        [255,     255,      255,      255,      255,      255,      255,      255]
    ])

print("img_A")
print(np.matrix(img_A))

img_B = np.array([
        [255,   255,    255,    255,    255,    255,    255,    255],
        [255,   255,    255,      0,      0,      0,      0,    255],
        [255,   255,    255,      0,      0,      0,      0,    255],
        [255,   255,    255,      0,      0,      0,      0,    255],
        [255,   255,    255,      0,      0,      0,      0,    255],
        [255,   255,    255,      0,      0,      0,      0,    255],
        [255,   255,    255,      0,      0,      0,      0,    255],
        [255,   255,    255,    255,    255,    255,    255,    255]
    ])

print("img_B")
print(np.matrix(img_B))

#Criação da imagem C através da multiplicação da matriz A com a B
img_C = []
for l in range(n):
    linha = []
    for c in range(n):
        if(img_A[l][c]-img_B[l][c]<0):
            linha.append(0)
        else:
            linha.append(img_A[l][c]-img_B[l][c])
    img_C.append(linha)

print('img C')
print(np.matrix(img_C))

plt.subplot(3,1,1), plt.imshow(img_A,"gray", vmin=0, vmax=255), plt.title('Imagem A'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,2), plt.imshow(img_B,"gray", vmin=0, vmax=255), plt.title('Imagem B'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,3), plt.imshow(img_C,"gray", vmin=0, vmax=255), plt.title('Imagem C'), plt.xticks([]), plt.yticks([])
plt.show()
