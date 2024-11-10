# Generated by Django 5.1.1 on 2024-11-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='bad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='good',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
