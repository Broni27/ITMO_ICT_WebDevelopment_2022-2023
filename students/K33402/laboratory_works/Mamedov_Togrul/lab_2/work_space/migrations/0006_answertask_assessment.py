# Generated by Django 4.1.4 on 2022-12-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_space', '0005_answertask'),
    ]

    operations = [
        migrations.AddField(
            model_name='answertask',
            name='assessment',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
