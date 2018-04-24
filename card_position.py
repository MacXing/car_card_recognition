import cv2
import numpy as np
from process_images import process_image
from correct_cart import correct_image
from findRegion import findPlateNumberRegion

def image_position(image):
    cv2.imshow('',image)
    cv2.waitKey(0)
    #灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #高斯平滑
    gaussian = cv2.GaussianBlur(gray, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
    median = cv2.medianBlur(gaussian, 5)
    # cv2.imshow('', median)
    # cv2.waitKey(0)
    #边缘检测
    sobel = cv2.Sobel(median, cv2.CV_8U, 1, 0, ksize=3)
    # cv2.imshow('', sobel)
    # cv2.waitKey(0)
    #二值化
    ret, binary = cv2.threshold(sobel, 170, 255, cv2.THRESH_BINARY)
    # cv2.imshow('', binary)
    # cv2.waitKey(0)
    # 膨胀和腐蚀操作的核函数
    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 6))
    # 膨胀一次，让轮廓突出
    dilation = cv2.dilate(binary, element2, iterations=1)
    # cv2.imshow('', dilation)
    # cv2.waitKey(0)
    # 腐蚀一次，去掉细节
    erosion = cv2.erode(dilation, element1, iterations=1)
    # cv2.imshow('', erosion)
    # cv2.waitKey(0)
    # 再次膨胀，让轮廓明显一些
    dilation2 = cv2.dilate(dilation, element2, iterations=1)
    # cv2.imshow('', dilation2)
    # cv2.waitKey(0)
    region = findPlateNumberRegion(dilation2)
    # print(region)
    # 用绿线画出这些找到的轮廓
    cImg = img.copy()
    for box in region:
        cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
        Xs = [i[0] for i in box]
        Ys = [i[1] for i in box]
        x1 = min(Xs)
        x2 = max(Xs)
        y1 = min(Ys)
        y2 = max(Ys)
        hight = y2 - y1
        width = x2 - x1
        cropImg = cImg[y1:y1 + hight, x1:x1 + width]

    cv2.imshow('1',img)
    cv2.waitKey(0)

    rotated = correct_image(cropImg)
    process_image(rotated)

if __name__ == '__main__':
    img = cv2.imread(r'D:\workspace\car_card_recognition\data\0.jpg')
    if img is not None:
        image_position(img)
    else:
        print("图片读入失败！")