import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters
from skimage import data, filters

# Cargar una imagen de ejemplo
image = data.chelsea()  # Imagen de un gato

# Mostrar la imagen
plt.imshow(image)
plt.axis('off')  # Desactivar ejes
plt.show()

# Aplicar filtro Gaussiano para suavizado
smooth_image = filters.gaussian(image, sigma=1)

# Mostrar imagen original y suavizada
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(image)
ax[0].set_title('Imagen original')
ax[0].axis('off')

ax[1].imshow(smooth_image)
ax[1].set_title('Imagen suavizada')
ax[1].axis('off')

plt.show()

from skimage import color

# Convertir la imagen a escala de grises (la detección de bordes suele usarse en un solo canal)
image_gray = color.rgb2gray(image)

# Aplicar filtro Sobel
edges = filters.sobel(image_gray)

# Mostrar bordes
plt.imshow(edges, cmap='gray')
plt.title('Bordes')
plt.axis('off')
plt.show()