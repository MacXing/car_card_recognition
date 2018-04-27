import requests
import json
import pymysql
import re
def insert_db(data):
    conn = pymysql.connect(host="192.168.160.36",user="root",
                           password="gzxiaoi",db="crawler",charset="utf8")
    sql = '''INSERT INTO TEMP_BAIKE_GY(G_ID,ISNEW,IMGURL,WIDTH,HEIGHT,LEMMATITLE,SUBLEMMAID,
              OLDLEMMAID,OLDSUBLEMMAID,CATEGORY,DESCS,LOVECNT,URL)
              VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor = conn.cursor()
    try:
        cursor.executemany(sql,data)
        conn.commit()
        print("Success!")
    except Exception as e:
        print(e)
    else:
        cursor.close()
        conn.close()

urls = []

for i in range(25):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    url ="http://www.mafengwo.cn/qa/ajax_qa/more?type=3&mddid=11239&tid=&sort=8&key=&page="+str(i)+"&time="
    data = requests.get(url=url,
                        headers =headers)
    data = json.loads(data.text)
    html = str(data['data'])
    hrefs = re.findall(r'/wenda/detail-\w*.html',html)
    urls = hrefs+urls
    print("Sucess %d page"%(i))

urls = list(set(urls))
print(len(urls))
with open(r'C:\Users\User\Desktop\马蜂窝.txt','w',encoding="utf-8") as f:
    for url in urls:
        f.write("http://www.mafengwo.cn"+url+'\n')


# result = []
# for d in data['data']:
#     if d['imgUrl'] == "":
#         d['imgUrl'] = "无"
#     if d['width'] == "":
#         d['width'] =0
#     if d['height'] =="":
#         d['height'] =0
#     result.append([d['id'],d['isNew'],str(d['imgUrl']),d['width'],
#                    d['height'],d['lemmaTitle'],d['subLemmaId'],
#                    d['oldLemmaId'],d['oldSubLemmaId'],d['category'],
#                    d['desc'],d['loveCnt'],"https://baike.baidu.com/view/"+str(d['oldLemmaId'])])
    # print(d['id'])
    # print(d['isNew'])

    # print(d['imgUrl'])
    # print(d['width'])
    # print(d['height'])
    # print(d['lemmaTitle'])
    # print(d['subLemmaId'])
    # print(d['oldLemmaId'])
    # print(d['oldSubLemmaId'])
    # print(d['category'])
    # print(d['desc'])
    # print(d['loveCnt'])
    # print("https://baike.baidu.com/view/"+str(d['oldLemmaId']))

# insert_db(result)