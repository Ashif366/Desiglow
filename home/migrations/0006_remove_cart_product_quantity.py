# Generated by Django 4.2.5 on 2023-09-23 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_cart_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_quantity',
        ),
    ]
