# Generated by Django 2.2.5 on 2019-09-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0005_auto_20190923_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(choices=[('S', 'Statement'), ('D', 'Doubt'), ('I', 'Imp'), ('W', 'Work')], default=3, max_length=200),
        ),
    ]