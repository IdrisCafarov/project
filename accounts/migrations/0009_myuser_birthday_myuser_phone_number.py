# Generated by Django 4.1 on 2022-09-10 11:52

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_myuser_company_name_alter_myuser_is_buyer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='birth date'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='phone number'),
        ),
    ]
