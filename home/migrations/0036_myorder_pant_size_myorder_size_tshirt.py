# Generated by Django 5.0.2 on 2024-03-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_cart_pant_size_cart_size_tshirt'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='pant_size',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='myorder',
            name='size_tshirt',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
    ]
