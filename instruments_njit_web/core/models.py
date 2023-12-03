from django.conf import settings
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    item_main_img = models.ImageField(default=False, upload_to=settings.STATIC_ROOT + "/imgs")

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.DateTimeField(default=False)
    def __str__(self):
        return self.title