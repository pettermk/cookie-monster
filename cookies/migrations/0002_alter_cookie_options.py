# Generated by Django 4.1 on 2022-08-31 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cookie',
            options={'ordering': ['time_sent']},
        ),
    ]
