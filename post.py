# coding=utf-8
import requests
import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance

def DecodeQR(image):
    img = Image.open(image)
    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        # print(barcodeData)
    de_url = barcodeData
    de_uid = barcodeData.split('=')[1]
    return de_url,de_uid

def PostData(url,uid):
    querystring = {"uid":uid}
    payload = "task=like"
    headers = {
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Origin': "https://act.dota2.com.cn",
        'X-Requested-With': "XMLHttpRequest",
        'User-Agent': "Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) > AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 > Chrome/37.0.0.0 Mobile Safari/537.36 > MicroMessenger/6.0.2.56_r958800.520 NetType/WIFI",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        # 'Cookie': "DOTA2=451e0f4ff214ac86d963b32fc0727d5c; isLogin=0,DOTA2=451e0f4ff214ac86d963b32fc0727d5c; isLogin=0;",
        'Cache-Control': "no-cache",
        # 'Postman-Token': "218183b9-4473-4924-a6d7-a9d34463b747,123206ec-9d2b-491f-b9f3-ccb6150a166d",
        'Host': "act.dota2.com.cn",
        'accept-encoding': "gzip, deflate",
        'content-length': "9",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    return response.text

if __name__ == "__main__":

    print('start')

    qr_image = '11.png'
    url,uid = DecodeQR(qr_image)
    print('解析QRcode:',url)

    for n in range(50):
        res = PostData(url,uid)
        print('\r',n+1,res,end="")

    print('\nend')
