# Generated by Django 5.1.1 on 2024-10-31 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_chosens_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chosens',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
