from django.conf import settings
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    item_main_img = models.ImageField(default=False, upload_to="default")

    def __str__(self):
        print(self.item_main_img)
        print(settings.BASE_DIR)
        print(settings.STATIC_ROOT)
        return self.title


    # Need to add a method that calls 
    def get_img_file_name():
        file_name = self.item_main_img.split('\\')
        print(item_main_img)
        return file_name

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