# Generated by Django 2.0 on 2018-11-20 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pproducts', '0002_auto_20181120_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_product',
            name='Average_Rating',
        ),
        migrations.RemoveField(
            model_name='p_product',
            name='Review_count',
        ),
    ]
