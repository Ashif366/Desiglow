# Generated by Django 4.2.5 on 2023-09-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_product_name_myorder_product_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='product_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
