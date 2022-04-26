# Generated by Django 4.0.4 on 2022-04-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_app', '0003_rename_param_name_quality_parameter_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quality',
            name='parameter_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quality',
            name='template_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]