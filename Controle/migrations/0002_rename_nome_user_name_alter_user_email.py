# Generated by Django 4.2.5 on 2023-09-21 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Controle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nome',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]