from spider_task import html_downloader
import urllib.request
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin 
import datetime

class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()

    num = 0

    def craw(self):

        # getting the page index.
        html_index = self.downloader.download("http://main.sgg.whu.edu.cn/gonggao/")
        soup = BeautifulSoup(html_index, 'html.parser')
        page_info = str(soup.find("span", "pageinfo"))
        page_count = int(re.search(r"\d+\.?\d*", page_info).group()) # we have page_count pages of bulletin
        urls = set()
        for i in range(1, page_count + 1):
            current_url = "http://main.sgg.whu.edu.cn/gonggao/list_10_%d.html" % i
            html_li = self.downloader.download(current_url)
            soup = BeautifulSoup(html_li, 'html.parser')
            for li in soup.find(class_="listbox").find_all('li'):
                tmp_url = li.a.get('href')
                true_url = urljoin(current_url, tmp_url)
                urls.add(true_url)
        #now we have all the page links. And we'll get the content.

        #parse the links we get.

        result = []  # save all the data in memory in anacceptable level.
        count = 1   # simply record the order. 

        special = {"http://main.sgg.whu.edu.cn/plus/view.php?aid=3871",
                    "http://main.sgg.whu.edu.cn/plus/view.php?aid=2247",
                    "http://main.sgg.whu.edu.cn/plus/view.php?aid=2318",
                    ""}
        # some links failed.

        for url in urls:
            title = 'None'
            time = ''
            content = 'None'
            page_cont = self.downloader.download(url)

            if page_cont is not None:
                if url not in special:
                    page_result = {}
                    page_soup = BeautifulSoup(page_cont, 'html.parser', from_encoding='gb2312')

                    # getting title, time, content.
                    reg_time = "([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-9])))"

                    cont_soup = page_soup.find(class_="page")

                    if cont_soup is not None:
                        title = cont_soup.find(id="pagetitle").get_text()
                        time = re.search(reg_time, str(cont_soup)).group()
                        content = cont_soup.find(class_="pagecon").get_text()
                    else:
                        content = "Failed to get content..."
                    
                # here we have some special cases with a diffrent domain...
                elif url in special:
                    if url == "http://main.sgg.whu.edu.cn/plus/view.php?aid=3871":
                        title = "关于提名2018年度《夏坚白测绘事业创业与科技创新奖》候选人的通知"
                        time = "2018-06-11"
                        content = "尊敬的各位专家:根据《夏坚白测绘事业创业与科技创新奖》奖励章程的规定，“创业与创新奖”通过提名方式产生候选人。提名人为测绘界院士、奖励顾问委员会委员、管理委员会委员和省级以上测绘主管部门的主要负责人，提名以通讯或书面方式进行。请您在百忙之中抽出时间..."
                    if url == "http://main.sgg.whu.edu.cn/plus/view.php?aid=2318":
                        title = "关于提名2014年度《夏坚白奖》候选人公告"
                        time = "2014-07-10"
                        content = "2014年度《夏坚白测绘事业创业与科技创新奖》推荐提名候选人工作已开始"
                    if url == "http://main.sgg.whu.edu.cn/plus/view.php?aid=2247":
                        title = "千人计划网_失效网页"
                # end of spacial
            
                page_result['title'] = title
                try:
                    page_result['time'] = [datetime.date(*map(int,time.split('-'))), time]
                    # 0 for datetime and 1 for isoformat'YYYY-MM-DD' string
                except ValueError:
                    print("时间格式转换失败……")
                page_result['source'] = url
                page_result['content'] = content[0:140] + '...' # the artical is always too long to print out.

                result.append(page_result) # add data to the dict.

            else:
                page_result = {
                    'title': '404 Not Found',
                    'time': '',
                    'content': 'None',
                    'source': url,
                }
                result.append(page_result)

            # we do not directly print out here.
            # pass the args to the frame and we'll format & print.

            count += 1
            if (self.num and (count > self.num)):
                return result   # 'num' to control the items number we get. 
            
        return result   # enhance robustness

if __name__=="__main__":
    obj_spider = SpiderMain()
    obj_spider.craw()
# 留下一个完整的测试接口备用