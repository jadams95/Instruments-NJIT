from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order, Payment
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import redirect
import random
import string
from .forms import CheckoutForm



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
    order_item, created = OrderItem.objects.get_or_create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
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

def remove_from_cart(request, slug):
        item = get_object_or_404(Item, slug=slug)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.items.filter(item__slug=item.slug).exists():
                order_item = OrderItem.objects.filter(item=item)[0]
                order.items.remove(order_item)
                order_item.delete()
                messages.info(request, "This item was removed from your cart.")
                
            else:
                messages.info(request, "This item was not in your cart.")
                return redirect("core:product", slug=slug)
        else:
            return redirect("core:product", slug=slug)
        return redirect("core:product", slug=slug)



def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the form data
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            shipped = form.cleaned_data.get('shipped')
            credit_card_number = form.cleaned_data.get('credit_card_number')
            expiration_date = form.cleaned_data.get('expiration_date')
            cvv = form.cleaned_data.get('cvv')

            # Save the order details to the database
            # (Assuming order and associated items already exist)
            payment = Payment.objects.create(
                email=email,
                address=address,
                shipped=shipped,
                credit_card_number=credit_card_number,
                expiration_date=expiration_date,
                cvv=cvv
            )

            # Perform any other necessary actions (e.g., payment processing)
            print(payment)
            return redirect('thank-you.html')  # Redirect to a success page after checkout
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'form': form})

def thankyou(request):
    return render(request, 'thank-you.html')