# Generated by Django 3.0.3 on 2020-04-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='produto',
            field=models.CharField(max_length=100),
        ),
    ]
