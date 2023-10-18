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

def showminji(request,slug):
    try:
        minji = Minji.objects.get(slug=slug) 
        if minji != None:
            return render(request,'minji.html',locals())
        else:
            return redirect("/")
    except:
        return redirect("/")
        #select * from minji where slug=%slug
    

'''
def homepage(request):
    minjis = Minji.objects.all()  #select * from minji
    minji_lists = list()
    for counter,minji in enumerate(minjis): #回傳2個值(索引值和資料)
        minji_lists.append(f'No. {counter}-{minji} <br>')
    return HttpResponse(minji_lists)
'''