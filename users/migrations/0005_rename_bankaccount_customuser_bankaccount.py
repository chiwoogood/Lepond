# Generated by Django 4.2.4 on 2025-01-09 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_address_detailaddress_address_extraaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='bankaccount',
            new_name='bankAccount',
        ),
    ]
