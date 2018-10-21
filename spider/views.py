from django.shortcuts import render
from spider_task import spider_main as sp
from .models import Bulletin
from django.http import HttpResponse

def func(request):
    print("Crawling data...Plz wait a few minutes.")
    obj = sp.SpiderMain()
    obj.num = 10    # to slice it
    for res in obj.craw():
        r = Bulletin(
            source = res['source'],
            title = res['title'],
            time = res['time'],
            content = res['content'],
        )
        r.save()
    return render(request, "spider/result.html")

def listing(request):
    latest_list = Bulletin.objects.all()
    context = {'latest_list' : latest_list}
    return render(request, 'spider/list.html', context) 

def searching():
    pass


