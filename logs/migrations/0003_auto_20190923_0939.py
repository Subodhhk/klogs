# Generated by Django 2.2.5 on 2019-09-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_auto_20190923_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(choices=[('S', 'Statement'), ('D', 'Doubt'), ('I', 'Imp')], default=0, max_length=200, unique=True),
        ),
    ]
