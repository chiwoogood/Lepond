# Generated by Django 4.2.4 on 2025-03-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='타이틀')),
                ('content', models.CharField(max_length=255, verbose_name='소개 내용')),
            ],
        ),
    ]
