import  cv2

# canny算子
img = cv2.imread('图片.jpg', 0)
blur = cv2.GaussianBlur(img, (3, 3), 0)  # 用高斯滤波处理原图像降噪
canny = cv2.Canny(blur, 50, 150)  # 50是最小阈值,150是最大阈值
cv2.imshow('canny', canny)
cv2.imwrite('canny.jpg', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

