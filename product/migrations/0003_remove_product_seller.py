# Generated by Django 4.1.1 on 2022-09-21 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
    ]
