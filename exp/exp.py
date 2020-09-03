# -*- encoding:utf-8 -*-
import sys
import os



# 调用app的路由方法

def hello_world():
    return '<h1> Hello World!</h1>'


def killport(port):
    command = '''kill -9 $(netstat -nlp | grep :''' + str(port) + ''' | awk '{print $7}' | awk -F"/" '{ print $1 }')'''
    os.system(command)


# 开始执行
if __name__ == '__main__':
    # 打开调试窗口
    # run可以指定host参数，指定ip,0.0.0.0表示全网段
    # app.run()
    port = 8080
    killport(port)


