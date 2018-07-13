import requests
import time as t
import cv2, os
import base64
from aip import AipOcr

APP_ID = '11508650'
API_KEY = 'xGOdD7LjKiTNREGKdILUhhkY'
SECRET_KEY = 'QQiGtNabtKIAC3FHIjTTph2uuvM8mQ9C'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def upload(pic):

    fileName = pic.split('/')[-1]
    file = {
        'logo' :(fileName, open(pic,'rb'), 'image/jpeg')
    }


    url1 = 'http://106.15.201.54:8080/sixGod/getMessage'
    #url2 = 'http://192.168.119.37:3000/upload'
    r = requests.post(url=url1, files=file)
    return r.content.decode()


def ROI(imgName):
    folder = os.path.exists('./temp')
    if not folder:
        os.mkdir('./temp')
    img = cv2.imread(imgName)
    shape  = img.shape
    img2 = img.copy()
    resized = cv2.resize(img, dsize=(1000, 500),interpolation=cv2.INTER_AREA)
    img_seal = resized[350:500, 550:1000]
    img_code = resized[30:80, 800:1000]
    seal = './temp/seal'+str(t.time())+'.jpg'
    code = './temp/code'+str(t.time())+'.jpg'
    cv2.imwrite(seal, img_seal)
    cv2.imwrite(code, img_code)
    return seal, code

def uploadd():
    TOKEN = '24.d001475b260542be4646a998b83ca5c9.2592000.1533698348.282335-11507767'
    body = {
        'image': ('4.jpg', open('C:/Users/Strider/Desktop/4.jpg', 'rb'), 'image/jpeg')
    }
    url= 'https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice?access_token='+TOKEN
    header = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
#    APPID = 'xGOdD7LjKiTNREGKdILUhhkY'
#    SECRETKEY = 'QQiGtNabtKIAC3FHIjTTph2uuvM8mQ9C'
    #print(body)
    #encodestr = base64.b64encode(body['image'])
    #print(str(encodestr, 'utf-8'))
    r = requests.post(url, data=body, headers=header)
    #return r.content.decode()

#print(uploadd())

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def up():
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content('C:/Users/Strider/Desktop/zwdd.jpg')
    dict = client.receipt(image)
    #print(client.receipt(image))
    sellercontent =[]
    '''
    res = {
        'seller': {
            'name' : dict['word_result']['SellerName'],
            'content': sellercontent
        }
    }
    '''
    print(dict)
#up()