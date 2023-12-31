from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    item_main_img = models.ImageField(default=False, upload_to="static")
    slug = models.SlugField(default=False)
    description = models.TextField(default=False)
    

    def __str__(self):
        print(self.item_main_img)
        print(settings.BASE_DIR)
        print(settings.STATIC_ROOT)
        return self.title


    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })
            
    def get_remove_from_cart(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


    

    # Need to add a method that calls 
    def get_img_file_name(self):
        return self.item_main_img

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    
    def __str__(self):
        # print(self)
        print(self.items)
        return f"order-id {self.user.username} of {self.items}"


class Payment(models.Model):
    email = models.EmailField(default=False)
    address = models.TextField(default=False)
    shipped = models.BooleanField(default=False)

    # Basic example for credit card (not recommended for production use)
    # In production, you should use a more secure method like using Stripe or similar payment gateways
    credit_card_number = models.CharField(default=False, max_length=16)
    expiration_date = models.DateField(default=False)
    cvv = models.CharField(default=False, max_length=4)
    
    
    def __str__(self):
        return f"User's email address for the order {self.email}"