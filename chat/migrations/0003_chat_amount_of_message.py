# Generated by Django 5.1.1 on 2024-10-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat_is_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='amount_of_message',
            field=models.IntegerField(default=0),
        ),
    ]
