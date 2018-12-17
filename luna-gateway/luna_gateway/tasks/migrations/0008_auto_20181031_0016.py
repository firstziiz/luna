# Generated by Django 2.1.2 on 2018-10-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20181030_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='task_desc',
        ),
        migrations.AddField(
            model_name='task',
            name='constrain_desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='task',
            name='examples',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='task',
            name='input_desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='task',
            name='output_desc',
            field=models.TextField(default=''),
        ),
    ]