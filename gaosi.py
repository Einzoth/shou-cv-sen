# encoding:utf-8
import cv2
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('图片.jpg')
source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 高斯滤波
result = cv2.GaussianBlur(source, (5, 5), 0)  # 可以更改核大小

# 显示图形
titles = ['Source Image', 'GaussianBlur Image (5, 5)']
images = [source, result]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


