# -*- enconding:utf-8 -*-
import cv2,string

from PIL import Image, ImageDraw, ImageFont
import random
def random_data():
    list = string.digits+string.ascii_uppercase
    list_digits = list[0:10]
    list_str = list[10:36]
    d1=[]
    for i in range(5):
        dig = random.randint(0,len(list_digits)-1)
        # print(dig)
        lstr = random.randint(0, len(list_str)-1)
        # print(lstr)
        ch = random.randrange(0,2)
        # print(ch)
        if ch ==1:
            d1.append(list_digits[dig])
        else:
            d1.append(list_str[lstr])
    print(d1)
    list_font = [chr(i) for i in range(65, 91)]
    d2 = list_font[random.randint(0,len(list_font)-1)]
    # print(d2)
    list_center = ["京","津","沪","渝","蒙","新","藏","宁","桂","港","澳","黑","吉","辽","晋","冀","青","鲁","豫",
    "苏","皖","浙","闽","赣","湘","鄂","粤","琼","甘","陕","贵","云","川"]
    d3 = list_center[random.randint(0,len(list_center)-1)]
    print(d3)
    return d1,d2,d3

def image(echpo):


    # 字体 字体*.ttc的存放路径一般是： /usr/share/fonts/opentype/noto/ 查找指令locate *.ttc
    # font = ImageFont.truetype('STXIHEI.TTF',29,encoding="utf-8")
    font = ImageFont.truetype('STXIHEI.TTF',70,encoding="utf-8")
    # 字体颜色

    fillColor = (255, 255, 255)
    # 文字输出位置
    position1 = (5,0)
    position2 = (80, 3)
    position3 = (185, 3)
    position4 = (245, 3)
    position5 = (310, 3)
    position6 = (380, 3)
    position7 = (440, 3)
    for e in range(echpo):
        img = cv2.imread('C:\\Users\\User\\Desktop\\2.jpg')  # 读取图片
        img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        d1,d2,d3 = random_data()
        # 输出内容
        str1 = d3
        str2 = d2
        str3 = d1[0]
        str4 = d1[1]
        str5 = d1[2]
        str6 = d1[3]
        str7 = d1[4]
        str_name=str1+str2+str3+str4+str5+str6+str7
        # 需要先把输出的中文字符转换成Unicode编码形式
        str_name=''+str_name

        draw = ImageDraw.Draw(img_PIL)
        draw.text(position1, str1, fill=fillColor,font=font)
        draw.text(position2, str2, fill=fillColor,font=font)
        draw.text(position3, str3, fill=fillColor,font=font)
        draw.text(position4, str4, fill=fillColor,font=font)
        draw.text(position5, str5, fill=fillColor,font=font)
        draw.text(position6, str6, fill=fillColor,font=font)
        draw.text(position7, str7, fill=fillColor,font=font)
        # 使用PIL中的save方法保存图片到本地
        img_PIL.save('H:\\毕业论文\\car_recognition\\image\\' +str_name+ '.jpg', 'jpeg')

# 转换回OpenCV格式
# img = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)
# cv2.imshow('demo',img)
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
# cv2.imwrite('D:\\workspace\\car_card_recognition\\image\\' +str_name+ '.jpg', img)
# cv2.imshow('You need to struggle', img)
# cv2.waitKey(0)
# 保存图片
# cv2.SaveImage('C:\\Users\\User\\Desktop\\3.jpg', img)

if __name__ == '__main__':
    image(100000)
    # random_data()