# Generated by Django 2.1.2 on 2018-10-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20180928_1850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['main_topic', 'order']},
        ),
        migrations.AddField(
            model_name='task',
            name='enable',
            field=models.BooleanField(default=True),
        ),
    ]
