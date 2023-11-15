from django.shortcuts import render
from mysite.models import Minji
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
    minjis = Minji.objects.all()
    now = datetime.now()
    return render(request, 'index.html' , locals())

def showminji(request, slug):
    try:
        minji = Minji.objects.get(slug=slug) 
        if minji != None:
            return render(request,'minji.html',locals())
        else:
            return redirect("/")
    except:
        return redirect("/")
        #select * from minji where slug=%slug

import random  
def about(request, num=-1):
    if num == -1 or num > 4:
        quotes = ['今日事今日畢',
                  '要怎麼收穫，先怎麼栽',
                  '知識就是力量',
                  '一個人的個性就是他的命運']
        quotes = random.choice(quotes)
    else:
        quotes = quotes[num]
    return render(request,'about.html',locals()) 


'''
def homepage(request):
    minjis = Minji.objects.all()  #select * from minji
    minji_lists = list()
    for counter,minji in enumerate(minjis): #回傳2個值(索引值和資料)
        minji_lists.append(f'No. {counter}-{minji} <br>')
    return HttpResponse(minji_lists)
'''