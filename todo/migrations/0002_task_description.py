# Generated by Django 3.1.2 on 2020-10-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]