# Generated by Django 4.1.1 on 2022-09-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_myuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_pro',
            field=models.BooleanField(default=False, verbose_name='pro seller'),
        ),
    ]
