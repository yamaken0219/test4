import urllib
import os
import requests
import datetime


now=datetime.date.today()
print(now)
year=now.year-2000
month=now.month
day=now.day
if month<10:
    month=str(month)
    month=str(0)+str(month)

if day<10:
    day=str(day)
    day=str(0)+str(day)

number=str(year)+str(month)+str(day)+"12"
print(number)



tenki="https://www.jma.go.jp/jp/g3/images/jp_c/"+number+".png"
pic=urllib.request.urlretrieve(tenki,"test.png")

url = "https://notify-api.line.me/api/notify"
access_token = '2DE8DXhOv3xdMzwjL0T54rNWPtXSu3GEVOav6ANbcfx'
headers = {'Authorization': 'Bearer ' + access_token}

message = '今日の天気図'
image = "test.png"  # png or jpg
payload = {'message': message}
files = {'imageFile': open(image, 'rb')}
r = requests.post(url, headers=headers, params=payload, files=files,)
