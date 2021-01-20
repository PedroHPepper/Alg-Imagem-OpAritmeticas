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

#As somas sempre são truncadas caso passe de 255, pois as matrizes são uint8, porém sempre ocorre um erro. Portanto é preciso fazer casting ou tirar as
#definições de uint8 das matrizes.

img_C = []
for l in range(3):
    linha = []
    for c in range(3):
        if(int(img_A[l][c]) + int(img_B[l][c])>255):
            linha.append(255)
        else:
            linha.append(int(img_A[l][c]) + int(img_B[l][c]))
    img_C.append(linha)

print(np.matrix(img_C))
plt.subplot(3,1,1), plt.imshow(img_A,"gray", vmin=0, vmax=255), plt.title('Imagem 1'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,2), plt.imshow(img_B,"gray", vmin=0, vmax=255), plt.title('Imagem 2'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,3), plt.imshow(img_C,"gray", vmin=0, vmax=255), plt.title('Imagem resultante da Soma'), plt.xticks([]), plt.yticks([])
plt.show()