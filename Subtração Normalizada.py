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

#Criação da imagem C através da subtração da matriz A com a B
img_C = []
for l in range(n):
    linha = []
    for c in range(n):
        linha.append(img_A[l][c]-img_B[l][c])
    img_C.append(linha)
print('Imagem 3 sem normalização')
print(np.matrix(img_C))
#Achar o maior e menor valor da matriz
maior = img_C[0][0]
menor = img_C[0][0]
for l in range(n):
    for c in range(n):
        if(maior<img_C[l][c]):
            maior=img_C[l][c]
        if(menor>img_C[l][c]):
            menor=img_C[l][c]

#Normalização
for l in range(n):
    for c in range(n):
        img_C[l][c] = int((255/(maior-menor))*(img_C[l][c]-menor))

print('img C')
print(np.matrix(img_C))

plt.subplot(3,1,1), plt.imshow(img_A,"gray", vmin=0, vmax=255), plt.title('Imagem A'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,2), plt.imshow(img_B,"gray", vmin=0, vmax=255), plt.title('Imagem B'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,3), plt.imshow(img_C,"gray", vmin=0, vmax=255), plt.title('Imagem C'), plt.xticks([]), plt.yticks([])
plt.show()
