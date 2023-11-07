import cv2 as cv
# Scharr算子
img = cv.imread('图片.jpg', 0)
x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=-1)
y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=-1)
# ksize=-1 Scharr算子
# cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
# 可选参数alpha是伸缩系数，beta是加到结果上的一个值，结果返回uint类型的图像
Scharr_absX = cv.convertScaleAbs(x)  # convert 转换  scale 缩放
Scharr_absY = cv.convertScaleAbs(y)
result = cv.addWeighted(Scharr_absX, 0.5, Scharr_absY, 0.5, 0)
cv.imshow('img', img)
cv.imshow('Scharr_absX', Scharr_absX)
cv.imshow('Scharr_absY', Scharr_absY)
cv.imshow('result', result)
cv.imwrite('img.jpg', img)
cv.imwrite('Scharr_absX.jpg', Scharr_absX)
cv.imwrite('Scharr_absY.jpg', Scharr_absY)
cv.imwrite('result.jpg', result)
cv.waitKey(0)
cv.destroyAllWindows()


