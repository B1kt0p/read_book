from django.shortcuts import render
from blog.models import Category, Good
from django.http import HttpResponse, Http404

# Create your views here.


def index(request, id):
    if  id==None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk=id)
    goods = Good.objects.filter(category=cat).order_by('name')
    s = 'Категория: {} {}'.format(cat.name, '<br><br>')
    for good in goods:
        s ='{s} ({good}) {name} <br>'.format(s=s, good=good.pk, name=good.name)
    return HttpResponse(s)


def good(request, id):
    try:
        good = Good.objects.get(pk=id)
    except Good.DoesNotExist:
        raise Http404
    s = good.name +'<br><br>'+good.category.name +'<br><br>'+good.description
    if not good.in_stock:
        s = s + '<br><br>' + 'Нет в наличии'
    return HttpResponse(s)


