'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/15 16:13
# @Author : chenxin
# @Site : 
# @File : socket_server.py
# @Software: PyCharm
import socket
#服务器端

server = socket.socket()
server.bind(('localhost',1234))#绑定要监听的端口
server.listen()#监听

print('我要开始等电话了')

conn,addr=server.accept()#等电话打进来
#conn就是客户端连过来而在服务器端为其生成的一个连接实例
print(conn,addr)


print('电话来了')
#data = server.recv(1024)
data = conn.recv(1024)
#server.recv(1024)
print('recv:',data)
#server.send(data.upper())
conn.send(data.upper())
server.close()
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/15 16:13
# @Author : chenxin
# @Site :
# @File : socket_server.py
# @Software: PyCharm
import socket
#服务器端

server = socket.socket()
server.bind(('localhost',1234))#绑定要监听的端口
server.listen(5)#监听 最大连接数
conn,addr=server.accept()#等电话打进来
    #conn就是客户端连过来而在服务器端为其生成的一个连接实例
print(conn,addr)
print('电话来了')
print('我要开始等电话了')
count = 0
while True:
    data = conn.recv(1024)
    print('recv:',data)
    if not data:
        print("dsl has lost...")
        break
    conn.send(data.upper())
    count +=1
    if count >10:break
server.close()



