# Generated by Django 5.1.1 on 2024-10-22 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chat_amount_of_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'Чат', 'verbose_name_plural': 'Чат'},
        ),
    ]
