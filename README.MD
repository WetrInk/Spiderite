# NOTES

*   [测院官网][site]可能存在**校园网无法访问**的情况，导致html获取失败。
    此时将会出现无法解析之类的错误。
    使用流量等其他网络通道可以解决。

    [site]: <http://main.sgg.whu.edu.cn/>

*   爬虫部分使用 Python 3.7 + [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) 编写。


# Logs

*   2018.10.21 
    *   1. 做了一些妥协，输出时仅选择默认输出前20项公告以提高速度
    *   2. 完善了List页面，统一规划了静态文件的处理
    *   3. (并没有清空数据库 保留了debug模式
    *   4. Search还没有做完(逃
    *   5. 还需要完善调用脚本方式(我觉得没有人会喜欢打开页面时干等几十秒)
