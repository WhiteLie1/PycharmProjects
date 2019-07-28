# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time : 2019/7/24 9:03
# # @Author : chenxin
# # @Site :
# # @File : PictureTest.py
# # @Software: PyCharm
'''import urllib.request, sys
import requests
import base64
url = 'https://api.yimei.ai/v2/api/face/analysis/131071'
client_id = "a2dadd45a7a8dc64";
client_secret = "19cece3586122e52a126bab0d9800c1b";
f = open('D:\Maindocuments\Mainsoftware\PycharmProjects\America_python\TestCode\images/test.jpg','rb')
bodys = {}
bodys['image'] = f
print(f)
post_data = urllib.parse.urlencode(bodys)
request = urllib.request.Request(url, post_data)
authorization = 'Basic ' + str(base64.b64encode((client_id+ ':' \
                   + client_secret).encode('utf-8')), 'utf-8')
print(authorization)
request.add_header('Authorization', authorization)
#根据API的要求，定义相对应的Content-Type
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)
'''


import requests,base64
url = 'https://api.yimei.ai/v2/api/face/analysis/131072'
client_id = "75915c227703ba83";
client_secret = "d4e72673ce5af4fcb0d980cd458b58f2";
authorization = 'Basic ' + str(base64.b64encode((client_id \
    + ':' + client_secret).encode('utf-8')), 'utf-8')
print(authorization)

headers = {'Authorization': authorization}
filename = 'D:\Maindocuments\Mainsoftware\PycharmProjects\America_python\TestCode\images/test.jpg'
files = {'image':(filename, open(filename,'rb'), "multipart/form-data")}
response = requests.post(url, headers=headers, files=files);

print(str(response.content,'utf-8'))
print(response.status_code)
