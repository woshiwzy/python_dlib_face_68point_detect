# coding:utf-8

import cv2
import cv2 as cv
import face_recognition
import numpy as np


def contrast_demo(img1, c, b):  # 亮度就是每个像素所有通道都加上b
    rows, cols, chunnel = img1.shape
    blank = np.zeros([rows, cols, chunnel], img1.dtype)  # np.zeros(img1.shape, dtype=uint8)
    dst = cv2.addWeighted(img1, c, blank, 1 - c, b)
    # cv.imshow(tartWindow, dst)
    return dst


def seekChanged(x):
    global seek
    seek = x
    global srcImage

    dst = contrast_demo(srcImage, 1.3, seek)

    cv.imshow(tartWindow, dst)

    face_locations = face_recognition.face_locations(dst)

    for rect in face_locations:
        org = (rect[0], rect[3])
        wh = (rect[2], rect[2])
        cv.rectangle(dst, org, wh, (255, 133, 133), thickness=3)

        print (face_locations[0])

    # time.sleep(10)
    cv.imshow("result", dst)

    print("light:" + str(x))

    if 27 == cv.waitKey():
        return


if __name__ == '__main__':

    srcWidnow = "src"
    tartWindow = "target"
    # filePath = "/Users/wangzy/test/lena.jpg"
    filePath = "/Users/wangzy/test/t.jpeg"
    seek = 0
    srcImage = cv.imread(filePath)
    cv.imshow(srcWidnow, srcImage)
    cv.createTrackbar("seek", srcWidnow, 0, 255, seekChanged)

    while True:
        # srcImage = face_recognition.load_image_file(filePath)
        print "seek is :", seek
        image = contrast_demo(srcImage, 1.3, seek)

        face_locations = face_recognition.face_locations(image) # (top, right, bottom, left)

        for rect in face_locations:
            org = (rect[0], rect[3])
            wh = (rect[2], rect[2])
            cv.rectangle(image, org, wh, (255, 133, 133), thickness=3)
            print (face_locations[0])
        # time.sleep(10)
        cv.imshow(tartWindow, image)
        if 27 == cv.waitKey():
            break
