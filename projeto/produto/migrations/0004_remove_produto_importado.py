# Generated by Django 3.0.3 on 2020-04-09 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20200409_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='importado',
        ),
    ]
