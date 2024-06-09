# Generated by Django 4.2.5 on 2023-09-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_photo/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(blank=True, choices=[('Health Care', 'Health Care'), ('Beauty Product', 'Beauty Product'), ('Organic', 'Organic'), ('Physiotherapy', 'Physiotherapy'), ('Hospital Eqquipment', 'Hospital Eqquipment'), ('Surgical Product', 'Surgical Product'), ('Lab Product', 'Lab Product')], max_length=99, null=True),
        ),
    ]
