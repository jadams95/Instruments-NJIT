# Generated by Django 4.2.7 on 2023-12-03 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_item_item_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_main_img',
            field=models.ImageField(default=False, upload_to='static'),
        ),
    ]
