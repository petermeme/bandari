# Generated by Django 4.2.10 on 2024-03-06 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_games'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Games',
            new_name='Game',
        ),
    ]
