# Generated by Django 2.2.5 on 2019-09-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_auto_20190923_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(choices=[('S', 'Statement'), ('D', 'Doubt'), ('I', 'Imp')], default=0, max_length=200),
        ),
    ]