# Generated by Django 4.1.7 on 2023-04-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_enable',
            field=models.BooleanField(default=False, verbose_name='是否显示'),
        ),
    ]
