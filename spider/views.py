from django.shortcuts import render
from spider_task import spider_main as sp
from .models import Bulletin
from django.http import HttpResponse
from datetime import date
import datetime

def func(request):
    print("Crawling data...Plz wait a few minutes.")
    obj = sp.SpiderMain()
    obj.num = 10    # to slice it
    for res in obj.craw():
        r = Bulletin(
            source = res['source'],
            title = res['title'],
            time = res['time'][1], # 0 for datetime and 1 for isoformat'YYYY-MM-DD' string
            content = res['content'],
        )
        r.save()
    return render(request, "spider/result.html")

def listing(request):
    latest_list = Bulletin.objects.all()
    context = {'latest_list' : latest_list}
    return render(request, 'spider/list.html', context) 

def searching(request):
    return render(request, 'spider/search.html')

def ContentSearch(request):
    text = request.POST['search1']
    result = Bulletin.objects.filter(title__contains=text)
    context = {'latest_list' : result}
    return render(request, 'spider/list.html', context)

def TimeSearch(request):
    start_date = date.fromisoformat(request.POST['timeStart'])
    end_date = date.fromisoformat(request.POST['timeEnd'])
    result = Bulletin.objects.filter(time__range=(start_date, end_date))
    context = {'latest_list' : result}
    return render(request, 'spider/list.html', context)
