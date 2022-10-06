# Generated by Django 4.1.1 on 2022-09-21 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad1_image', models.ImageField(null=True, upload_to='ads', verbose_name='Ad1 Image')),
                ('link1', models.CharField(max_length=1500, null=True, verbose_name='Link 1')),
                ('ad2_image', models.ImageField(null=True, upload_to='ads', verbose_name='Ad2 Image')),
                ('link2', models.CharField(max_length=1500, null=True, verbose_name='Link 2')),
                ('ad3_image', models.ImageField(null=True, upload_to='ads', verbose_name='Ad3 Image')),
                ('link3', models.CharField(max_length=1500, null=True, verbose_name='Link 3')),
                ('ad4_image', models.ImageField(null=True, upload_to='ads', verbose_name='Ad4 Image')),
                ('link4', models.CharField(max_length=1500, null=True, verbose_name='Link 4')),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='Slug')),
                ('image', models.ImageField(null=True, upload_to='category_img', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Sub Category Name')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='Slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.maincategory', verbose_name='Choose Category')),
            ],
            options={
                'verbose_name': 'Sub Category',
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('description', models.TextField(verbose_name='About Product')),
                ('price', models.FloatField(verbose_name='Price')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='Slug')),
                ('image', models.ImageField(upload_to='products_img', verbose_name='Image')),
                ('draft', models.BooleanField(default=True, verbose_name='Shared')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated_Date')),
                ('discount_percent', models.FloatField(default=0)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='product.subcategory', verbose_name='Sub Category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_product', to=settings.AUTH_USER_MODEL, verbose_name='Store')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
