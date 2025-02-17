# Generated by Django 4.1.7 on 2023-02-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_space', '0008_alter_createtask_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertask',
            name='answer',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answertask',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='createtask',
            name='data_finish',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='createtask',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='createtask',
            name='sanctions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='createtask',
            name='task',
            field=models.TextField(null=True),
        ),
    ]
