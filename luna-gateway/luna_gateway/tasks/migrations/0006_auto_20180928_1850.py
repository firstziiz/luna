# Generated by Django 2.1.1 on 2018-09-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20180928_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='secondary_topics',
            field=models.ManyToManyField(blank=True, related_name='_task_secondary_topics_+', to='topics.TopicLevel'),
        ),
    ]