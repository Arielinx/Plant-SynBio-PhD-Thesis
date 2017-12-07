# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:59:15 2017

@author: Teoric
"""

from skimage import io #Importar libreria para importar imagen
from skimage import img_as_float #para transformar una imagen a valores entre 0 y 1
from skimage.color import rgb2gray #para pasar una imagen a escala de grises
import matplotlib.pyplot as plt #Importar libreria para graficos
import scipy.ndimage as ndi #para hacer el median filter sin alterar la foto en calidad, el de skimage si lo hace
from skimage import exposure #para el histograma del codigo
from skimage import filters #filtro otsu

foto = io.imread("ConstructoA0024.tif")
foto2 = img_as_float(foto)
foto3 = rgb2gray (foto2)
foto4 = ndi.median_filter (foto3, size=9)

#Filtros Otsu

#thres3 = filters.threshold_otsu(foto3)
#thres4 = filters.threshold_otsu(foto4)

#Filtros Triangle Anda mucho mejor! Encuentra lo que manualmente encuentras con el histograma

thres3t = filters.threshold_triangle (foto3)
thres4t = filters.threshold_triangle (foto4)

histograma = exposure.histogram(foto3)
histograma2 = exposure.histogram(foto4)
#plt.plot (histograma[1][215:255],histograma[0][215:255]) #para graficar
#plt.plot (histograma2[1][225:240],histograma2[0][225:240])


thres5 =0.92 #valor obtenido por inspeccion visual del histograma

ig, ax = plt.subplots(3, 3, figsize=(20, 20))

ax[0,0].imshow(foto2, cmap=plt.cm.gray)
ax[0,0].set_title('Original Color')

ax[0,1].imshow(foto3, cmap=plt.cm.gray)
ax[0,1].set_title('Original Grises')

ax[0,2].imshow(foto4, cmap=plt.cm.gray)
ax[0,2].set_title('Original Grises + Median')

ax[1,0].imshow(foto3, cmap=plt.cm.gray)
#ax[1,0].set_title('Original Grises + Otsu Color')

ax[1,1].imshow(foto3 < thres3t, cmap=plt.cm.gray)
#ax[1,1].set_title('Original Grises + Otsu Grises')

ax[1,2].imshow(foto3 < thres4t, cmap=plt.cm.gray)
#ax[1,2].set_title('Original Grises + Otsu Median')

ax[2,0].imshow(foto4, cmap=plt.cm.gray)
#ax[2,0].set_title('Original G/M + Otsu Color')

ax[2,1].imshow(foto4 < thres3t, cmap=plt.cm.gray)
#ax[2,1].set_title('Original G/M + Otsu Grises')

ax[2,2].imshow(foto4 < thres4t, cmap=plt.cm.gray)
#ax[2,2].set_title('Original G/M + Otsu Median')


#Going further: Otsu thresholding with adaptative threshold. For images with non-uniform illumination, it is possible to extend Otsu's method to the case for which different thresholds are used in different regions of space.

