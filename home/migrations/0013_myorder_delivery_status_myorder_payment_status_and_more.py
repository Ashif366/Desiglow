# Generated by Django 4.2.5 on 2023-09-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_myorder_product_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='delivery_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myorder',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myorder',
            name='shipped_status',
            field=models.BooleanField(default=False),
        ),
    ]
