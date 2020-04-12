# -*- coding: utf-8 -*-
# @Author: Catcher
# @Date: 2020-04-12 17:17:40
# @Email: catcheryp@gmail.com
# @Last Modified by: Catcher
# @Last Modified time: 2020-04-12 19:37:59

from flask import Flask, send_from_directory, redirect, url_for, request, jsonify
from flask_sse import sse
import time
import subprocess

app = Flask(__name__)
# redis路径
app.config["REDIS_URL"] = "redis://localhost"
# app注册sse的蓝图,并且访问路由是/stream1
app.register_blueprint(sse, url_prefix='/stream')

# 重定向到发送消息页面
@app.route('/')
def index():
    return redirect(url_for('.index', _external=True) + 'upload/' + 'index.html')

# 接收send_messages.html文件中接口发送的数据，并且通过sse实时推送给用户
@app.route('/messages', methods=['GET'])
def send_messages():
    #channel = request.values.get('channel')
    channel = 'log'
    #message = request.values.get('message')
    p = subprocess.Popen('tail -f ./test.log', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)    #起一个进程，执行shell命令
    while True:
        line = p.stdout.readline()   #实时获取行
        if line:                     #如果行存在的话
            message = str(line.strip())
            sse.publish({"message": message}, type='social', channel=channel)
    return jsonify({'code': 200, 'errmsg': 'success', 'data': None})

@app.route('/upload/<path:path>')
def send_file(path):
    return send_from_directory('upload/', path)

if __name__ == '__main__':
    app.run()
