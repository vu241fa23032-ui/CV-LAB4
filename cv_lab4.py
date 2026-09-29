import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_filtering(img,kernel,p=0,s=1):
  k_s=kernel.shape[0]
  m = (img.shape[0] - k_s) // s + 1
  n = (img.shape[1] - k_s) // s + 1
  filtered_img=np.zeros((m,n))
  for i in range(m):
    for j in range(n):
      filtered_img[i,j]=np.sum(kernel*img[i*s:i*s+k_s, j*s:j*s+k_s])
  return filtered_img

img=cv2.imread("/content/drive/MyDrive/dove.jpg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
k_s=9

kernel = np.ones( (k_s, k_s),dtype=np.float32) / (k_s * k_s)
filtered_image=image_filtering(grayscale,kernel)

plt.figure(figsize=(15,15))
plt.subplot(2, 2, 1)
plt.imshow(grayscale, cmap="gray")
plt.title("Original")

plt.subplot(2, 2, 2)
plt.imshow(filtered_image, cmap="gray")
plt.title("Filtered")
plt.show()

print("original size",img.shape)
print("filtered size",filtered_image.shape)
