from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2


img = Image.open('orginal.jpg').convert('RGB')
img = np.uint8(img)

imgr = img[:,:,0]
imgg = img[:,:,1]
imgb = img[:,:,2]

claher = cv2.createCLAHE(clipLimit=3, tileGridSize=(10,18))
claheg = cv2.createCLAHE(clipLimit=2, tileGridSize=(10,18))
claheb = cv2.createCLAHE(clipLimit=1, tileGridSize=(10,18))
cllr = claher.apply(imgr)
cllg = claheg.apply(imgg)
cllb = claheb.apply(imgb)

rgb_img = np.dstack((cllr,cllg,cllb))

plt.subplot(1,2,1),plt.imshow(img)
plt.title('原图'),plt.axis('off')
plt.subplot(1,2,2),plt.imshow(rgb_img)
cv2.imwrite("rgb.jpg",rgb_img)
plt.title('Clahe'),plt.axis('off')

plt.show()
