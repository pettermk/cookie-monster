# Generated by Django 4.1 on 2022-09-01 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookies', '0002_alter_cookie_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cookie',
            options={'ordering': ['-time_sent']},
        ),
    ]