from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.conf import settings



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def homepage(request):
    return render(request, "Index.html")

def productpage(request):
    return render(request, "Product.html")

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    print(Item.objects.all)
    print(settings.STATIC_ROOT)
    return render(request, "item_list.html", context)