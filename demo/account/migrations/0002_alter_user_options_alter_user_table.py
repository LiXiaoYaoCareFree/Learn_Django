# Generated by Django 5.1.6 on 2025-02-11 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户信息'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
