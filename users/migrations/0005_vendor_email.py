# Generated by Django 4.1.1 on 2022-10-22 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_vendor_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
