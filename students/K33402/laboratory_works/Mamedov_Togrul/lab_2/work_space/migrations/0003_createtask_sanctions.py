# Generated by Django 4.1.4 on 2022-12-18 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_space', '0002_createtask_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='createtask',
            name='sanctions',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
