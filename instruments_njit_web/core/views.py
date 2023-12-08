from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item
from django.conf import settings



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def homepage(request):
    return render(request, "Index.html")

def productpage(request):
    return render(request, "Product.html")

class HomeView(ListView):
    model = Item
    template_name = "Index.html"

    def item_list(request):
        context = {
            'home': Item.objects.all()
        }
        print(Item.objects.all)
        print(settings.STATIC_ROOT)
        return render(request, "Index.html", context)

class ItemDetailView(DetailView):
    model = Item
    template_name = "Product.html"  
    def product_req(request):
        context = {
            'product': Item.objects.all()
        }
        return render(request, "Product.html", context)