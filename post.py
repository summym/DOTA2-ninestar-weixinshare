import requests

uid = input("输入UID：")
url = "https://act.dota2.com.cn/ti9Event/share"

querystring = {"uid":uid}

payload = "task=like"
headers = {
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Origin': "https://act.dota2.com.cn",
    'X-Requested-With': "XMLHttpRequest",
    'User-Agent': "Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) > AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 > Chrome/37.0.0.0 Mobile Safari/537.36 > MicroMessenger/6.0.2.56_r958800.520 NetType/WIFI",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    'Cookie': "DOTA2=451e0f4ff214ac86d963b32fc0727d5c; isLogin=0,DOTA2=451e0f4ff214ac86d963b32fc0727d5c; isLogin=0;",
    'Cache-Control': "no-cache",
    'Postman-Token': "218183b9-4473-4924-a6d7-a9d34463b747,123206ec-9d2b-491f-b9f3-ccb6150a166d",
    'Host': "act.dota2.com.cn",
    'accept-encoding': "gzip, deflate",
    'content-length': "9",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
n = 0
while n < 50:
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)
    n+=1
print("Done")