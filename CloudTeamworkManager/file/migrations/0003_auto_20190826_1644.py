# Generated by Django 2.2 on 2019-08-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_appendix_filesize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appendix',
            name='upload_date',
            field=models.DateField(auto_now_add=True, verbose_name='上传日期'),
        ),
    ]
