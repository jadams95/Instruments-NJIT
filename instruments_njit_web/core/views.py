from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import redirect
import random
import string



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

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user)
    if order_qs.exists():
        order = order_qs[0]
        print(order)
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("core:product", slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("core:product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:product", slug=slug)