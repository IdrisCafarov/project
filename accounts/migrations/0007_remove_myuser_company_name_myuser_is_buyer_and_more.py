# Generated by Django 4.1 on 2022-09-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_myuser_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='company_name',
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_buyer',
            field=models.BooleanField(default=False, verbose_name='user type'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_seller',
            field=models.BooleanField(default=False, verbose_name='user type'),
        ),
    ]