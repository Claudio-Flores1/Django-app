# Generated by Django 4.1 on 2022-11-18 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_pieces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='piece_name',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
