# Generated by Django 4.1.7 on 2023-02-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='get',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
    ]
