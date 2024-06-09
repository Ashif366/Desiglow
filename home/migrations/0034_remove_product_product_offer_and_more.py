# Generated by Django 5.0.2 on 2024-03-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_product_product_wholesale_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_offer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_wholesale_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(blank=True, choices=[('T-Shirt', 'T-Shirt'), ('Shirt', 'Shirt'), ('Winter Jacket', 'Winter Jacket'), ('Jeans', 'Jeans'), ('Panjabi', 'Panjabi'), ('Pajama', 'Pajama'), ('Polo', 'Polo'), ('Tops & T-Shirt', 'Tops & T-Shirt'), ('Kamiz/Kurti', 'Kamiz/Kurti'), ('Wallet', 'Wallet'), ('Bag', 'Bag'), ('Cap', 'Cap'), ('Sunglasses', 'Sunglasses')], max_length=99, null=True),
        ),
    ]
