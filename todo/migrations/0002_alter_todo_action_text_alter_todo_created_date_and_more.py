# Generated by Django 4.0.6 on 2022-08-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='action_text',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='type',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
