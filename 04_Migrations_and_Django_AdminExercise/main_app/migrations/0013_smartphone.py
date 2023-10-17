# Generated by Django 4.2.4 on 2023-10-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_migrate_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('category', models.CharField(default='empty', max_length=20)),
            ],
        ),
    ]
