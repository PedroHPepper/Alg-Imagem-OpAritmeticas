import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (8.0, 8.0)

n = 8

# 8x8 source image
img_A = np.array([
        [0, 0,        0,        0,      0,          0,      0,          0],
         [2,   0,   0,  17,  54, 115, 206, 255],
         [8,  12,   6,  44, 118, 240, 255, 255],
         [18,  24,  30,  71, 182, 255, 255, 255],
         [32,  40,  48,  56, 246, 255, 255, 255],
         [50,  60,  70,  80,  90, 255, 255, 255],
         [72,  84,  96, 108, 120, 132, 255, 255],
         [98, 112, 126, 140, 154, 168, 182, 255]

],np.uint8)

print("img_A")
print(np.matrix(img_A))

img_B = np.array([
    [50, 40, 30, 20, 80, 90, 90, 80],
    [30, 40, 50, 100, 70, 100, 60, 70],
    [1, 4, 5, 3, 34, 8, 70, 60],
    [6, 7, 200, 100, 10, 90, 100, 3],
    [10, 9, 7, 6, 59, 30, 40, 40],
    [9, 6, 10, 8, 255, 200, 50, 40],
    [6, 9, 8, 7, 1, 3, 200, 100],
    [7, 8, 7, 8, 5, 2, 50, 30]
],np.uint8)

print("img_B")
print(np.matrix(img_B))

#As os pixels são sempre truncadas caso passe de 255, pois as matrizes são uint8, porém sempre ocorre um erro. Portanto é preciso fazer casting ou tirar as
#definições de uint8 das matrizes.
#Criação da imagem C através da multiplicação da matriz A com a B
img_C = []
for l in range(n):
    linha = []
    for c in range(n):
        linha.append(int(img_A[l][c])*int(img_B[l][c]))
    img_C.append(linha)

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
