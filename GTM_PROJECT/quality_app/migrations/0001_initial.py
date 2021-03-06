# Generated by Django 4.0.4 on 2022-04-22 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=120)),
                ('l_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('param_name', models.CharField(max_length=120)),
                ('error_description', models.CharField(max_length=500)),
                ('weightage', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality_app.user')),
            ],
        ),
    ]
