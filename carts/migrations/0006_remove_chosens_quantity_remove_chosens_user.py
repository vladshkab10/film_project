# Generated by Django 5.1.1 on 2024-10-31 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_chosens_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chosens',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='chosens',
            name='user',
        ),
    ]
