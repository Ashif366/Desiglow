# Generated by Django 4.2.5 on 2023-09-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_review_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='payment_details',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
