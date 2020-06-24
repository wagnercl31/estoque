# Generated by Django 2.2.12 on 2020-06-24 00:47

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_auto_20200518_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='data_entrada',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 23, 21, 47, 18, 838822), null=True),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='nf',
            field=models.PositiveIntegerField(null=True, verbose_name='nota fiscal'),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='quantidade',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
