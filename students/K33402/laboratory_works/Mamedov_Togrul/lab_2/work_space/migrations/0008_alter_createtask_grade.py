# Generated by Django 4.1.7 on 2023-02-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_space', '0007_alter_createtask_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createtask',
            name='grade',
            field=models.IntegerField(null=True),
        ),
    ]
