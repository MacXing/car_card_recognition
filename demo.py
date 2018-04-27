import cv2
from card_position import image_position
from correct_cart import correct_image
from process_images import process_image
from char_recognition import prediction

def main(img):
    #返回车牌定位
    cropImg = image_position(img)
    #车牌倾斜矫正
    rotated = correct_image(cropImg)
    #分割字符
    images = process_image(rotated)
    #预测
    prediction(images)

if __name__ == '__main__':
    img = cv2.imread(r'D:\workspace\car_card_recognition\data\0.jpg')
    if img is not None:
        main(img)
    else:
        print("图片读入失败！")