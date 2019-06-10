# coding:utf-8
import cv2 as cv
import numpy as np


def detect_circle_demo(image):
    # dst = cv.bilateralFilter(image, 0, 150, 5)  #高斯双边模糊，不太好调节,霍夫噪声敏感，所以要先消除噪声
    # cv.imshow("1",dst)
    # dst = cv.pyrMeanShiftFiltering(image,5,100)  #均值迁移，EPT边缘保留滤波,霍夫噪声敏感，所以要先消除噪声
    # cv.imshow("2", dst)

    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, image = cv.threshold(image, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)


    # dst = cv.GaussianBlur(image, (13, 15), 15)  # 使用高斯模糊，修改卷积核ksize也可以检测出来
    # # cv.imshow("3", dst)
    # gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(thresh, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))

    print("size:",len(circles))
    global src
    for i in circles[0, :]:
        cv.circle(src, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(src, (i[0], i[1]), 2, (255, 0, 0), 2)  # 圆心

    cv.imshow("detect_circle_demo", src)

src = cv.imread("/Users/wangzy/Pictures/icons.jpg")  # 读取图片
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)  # 创建GUI窗口,形式为自适应
cv.imshow("input image", src)  # 通过名字将图像和窗口联系

detect_circle_demo(src)

cv.waitKey(0)  # 等待用户操作，里面等待参数是毫秒，我们填写0，代表是永远，等待用户操作
cv.destroyAllWindows()  # 销毁所有窗口
