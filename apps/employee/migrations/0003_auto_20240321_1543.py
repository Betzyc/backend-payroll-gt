# Generated by Django 3.2.4 on 2024-03-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20240321_0331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='data_completion',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='data_hiring',
        ),
        migrations.AddField(
            model_name='employee',
            name='date_completion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='date_hiring',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='head_department',
            field=models.BooleanField(default=False),
        ),
    ]
