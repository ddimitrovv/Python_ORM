# Generated by Django 4.2.4 on 2023-10-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_product_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(max_length=150),
        ),
    ]
