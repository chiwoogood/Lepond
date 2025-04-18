# Generated by Django 4.2.20 on 2025-04-06 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_cartitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='introduce',
        ),
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
        migrations.CreateModel(
            name='ProductThumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_thumbnails/', verbose_name='썸네일 이미지')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbnails', to='shop.product')),
            ],
        ),
    ]
