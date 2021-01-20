import cv2
import numpy as np
import matplotlib.pyplot as plt



img_A = np.array([
    [200,100,100],
    [0,10,50],
    [50,250,120]
],np.uint8)


img_B = np.array([
    [100,220,230],
    [45,95,120],
    [205,100,0]
],np.uint8)


img_C = []
maior=int(img_A[0][0]) + int(img_B[0][0])
menor=int(img_A[0][0]) + int(img_B[0][0])


for l in range(3):
    linha = []
    for c in range(3):
        linha.append(int(img_A[l][c]) + int(img_B[l][c]))
        if(int(img_A[l][c]) + int(img_B[l][c]) > maior):
            maior = int(img_A[l][c]) + int(img_B[l][c])
        if(int(img_A[l][c]) + int(img_B[l][c]) < menor):
            menor = int(img_A[l][c]) + int(img_B[l][c])
    img_C.append(linha)

for l in range(3):
    for c in range(3):
        img_C[l][c] = int((255/(maior-menor))*(img_C[l][c]-menor))


print(np.matrix(img_C))
plt.subplot(3,1,1), plt.imshow(img_A,"gray", vmin=0, vmax=255), plt.title('Imagem 1'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,2), plt.imshow(img_B,"gray", vmin=0, vmax=255), plt.title('Imagem 2'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,3), plt.imshow(img_C,"gray", vmin=0, vmax=255), plt.title('Imagem resultante da Soma e Normalização'), plt.xticks([]), plt.yticks([])
plt.show()