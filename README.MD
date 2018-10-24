# NOTES

*   [测院官网][site]可能存在**校园网无法访问**的情况，导致html获取失败。
    此时将会出现无法解析之类的错误。
    使用移动等其他网络出口可以解决。

    [site]: <http://main.sgg.whu.edu.cn/>


# GUIDE

*   需要 | Requirements :
    *   [Python3.7](https://www.python.org/downloads/)
    *   
    *   [Django2.1](https://www.djangoproject.com/download/)
    *   [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
    *   \* Don't you like pip install \*


*   以下为参数：
    *   project: spiderite
    *   app: spider, django_web
    *   static: /static
    *   Setting.py:
        *   DEBUG = True
    *   admin: admin/123456     
    *   默认每次抓取公告数量：spider/views.obj.num = 10


## Logs

*   2018.10.21 
       1. 做了一些妥协，输出时仅选择默认输出前20项公告以提高速度
       2. 完善了List页面，统一规划了静态文件的处理
       3. (并没有清空数据库 保留了debug模式
       4. Search还没有做完(逃
       5. 还需要完善调用脚本方式(我觉得没有人会喜欢打开页面时干等几十秒)

*   2018.10.23  13:20
       1. 发现静态文件调用格式错误 导致CSS样式调用失败 已修复
       2. 默认抓取数量参数不符合设置 正在解决...

*   2018.10.24  21:40
       1. 完成了search部分
       2. 重置了数据库
       3. 增加了一个管理页面
