# Generated by Django 2.1.1 on 2018-09-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_topiclevel_outcome'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
