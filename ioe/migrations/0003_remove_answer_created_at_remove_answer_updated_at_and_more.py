# Generated by Django 4.1.1 on 2022-11-06 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ioe', '0002_answer_created_at_answer_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='question',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='question',
            name='updated_at',
        ),
    ]