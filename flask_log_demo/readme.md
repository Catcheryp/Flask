## 日志实时显示脚本

---

#### 说明
1.版本python2.7+
2.依赖的库

```
Flask
Flask-SSE
gevent
redis
gunicorn
```

3.`test.py` 是实时的向test.log里面写内容，测试使用

4.将`test.log`的内容实时显示在页面

#### 执行

```
gunicorn sse:app --worker-class gevent --workers 4 --bind 127.0.0.1:5000

#指定工作方式，这里用 gevent，表示使用异步
--worker-class gevent 

#用于处理工作进程的数量
--workers 4
```



#### 参考
[https://flask-sse.readthedocs.io/en/latest/](https://flask-sse.readthedocs.io/en/latest/)<br>
[https://github.com/Rgcsh/sse_chait](https://github.com/Rgcsh/sse_chait)<br>
[https://frostming.com/2017/04-05/flask-shi-xian-yuan-cheng-ri-zhi-shi-shi-jian-kong](https://frostming.com/2017/04-05/flask-shi-xian-yuan-cheng-ri-zhi-shi-shi-jian-kong)
