# Generated by Django 3.2.20 on 2023-09-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0003_teachermodel_t_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='t_email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='t_phone',
            field=models.CharField(max_length=100),
        ),
    ]
