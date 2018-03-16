# -*- enconding:utf-8 -*-
import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

img = cv2.imread('C:\\Users\\User\\Desktop\\0.png')  # 读取图片

img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# 字体 字体*.ttc的存放路径一般是： /usr/share/fonts/opentype/noto/ 查找指令locate *.ttc
# font = ImageFont.truetype(40)
# 字体颜色
fillColor = (255, 255, 255)
# 文字输出位置
position = (23, 30)
# 输出内容
str = 'H'

# 需要先把输出的中文字符转换成Unicode编码形式
str= str.encode('utf-8')

draw = ImageDraw.Draw(img_PIL)
draw.text(position, str, fill=fillColor)
# 使用PIL中的save方法保存图片到本地
# img_PIL.save('02.jpg', 'jpeg')

# 转换回OpenCV格式
img = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)
cv2.imshow('demo',img)
# 在刚才创建的窗口中显示图片

# cv2.IMREAD_COLOR：读入彩色图像，默认参数，Opencv 读取彩色图像为BGR模式 ！！！注意
# cv2.IMREAD_GRAYSCALE：读入灰度图像。
#云
# img = img[:,0:24]
#D
# img = img[:,30:55]
#s
# img = img[:,55:76]
#B
# img = img[:,77:100]
#1
# img = img[:,101:123]
#1
# img = img[:,124:148]
#0
# img = img[:,149:171]
#显示文字
#字体：FONT_HERSHEY_COMPLEX
# imageText = img.copy()
# print(imageText.shape[0])
# cv2.putText(imageText, '贵', (23,30), cv2.FONT_HERSHEY_DUPLEX, 5, (255, 255 ,255), thickness = 2, lineType = 5)
# cv2.imshow('Show text FONT_HERSHEY_COMPLEX', imageText)
# cv2.imwrite('./meinv2_text_' + 'FONT_HERSHEY_COMPLEX' + '.jpg', imageText)
# cv2.imshow('You need to struggle', img)
cv2.waitKey(0)
# 保存图片
# cv2.SaveImage('C:\\Users\\User\\Desktop\\0_0.png', img)