# Generated by Django 4.1.1 on 2022-09-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_myuser_birthday_myuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='usertype',
            field=models.IntegerField(blank=True, choices=[(1, 'Man'), (2, 'Woman')], null=True, verbose_name='Cins'),
        ),
    ]
