# Generated by Django 4.2.4 on 2025-03-06 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_alter_qna_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='QnaInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='공지 제목')),
                ('content', models.TextField(blank=True, null=True, verbose_name='공지 내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('is_published', models.BooleanField(default=True, verbose_name='공개 여부')),
            ],
            options={
                'verbose_name': 'Q&A 공지사항',
                'verbose_name_plural': 'Q&A 공지사항 목록',
                'ordering': ['-created_at'],
            },
        ),
    ]
