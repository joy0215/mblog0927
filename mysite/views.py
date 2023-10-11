from django.shortcuts import render
from mysite.models import Minji
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def homepage(request):
    minjis = Minji.objects.all()
    now = datetime.now()
    return render(request, 'index.html' , locals())

def showminji(request,slug):
    minji = Minji.objects.get(slug=slug) 
    #select * from minji where slug=%slug
    return render(request,'minji.html',locals())
    

'''
def homepage(request):
    minjis = Minji.objects.all()  #select * from minji
    minji_lists = list()
    for counter,minji in enumerate(minjis): #回傳2個值(索引值和資料)
        minji_lists.append(f'No. {counter}-{minji} <br>')
    return HttpResponse(minji_lists)
'''