# Generated by Django 4.1.3 on 2022-11-08 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_topic_alter_question_codecheflink_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='global_check',
        ),
    ]
