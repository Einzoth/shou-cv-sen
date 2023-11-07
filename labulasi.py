import cv2
# 拉普拉斯算子
img = cv2.imread('1281.jpg', 0)
blur = cv2.GaussianBlur(img, (3, 3), 0)
laplacian = cv2.Laplacian(blur, cv2.CV_16S, ksize=3)
dst = cv2.convertScaleAbs(laplacian)
cv2.imshow('laplacian', dst)
cv2.imwrite('laplacian.jpg', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()




