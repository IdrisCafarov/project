# Generated by Django 4.1.1 on 2022-11-18 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_vendor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_vendor', to=settings.AUTH_USER_MODEL),
        ),
    ]
