# Generated by Django 4.0.5 on 2022-07-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_testcrud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=200)),
                ('data_id', models.CharField(max_length=200)),
                ('device_type', models.CharField(max_length=200)),
                ('consumption', models.CharField(max_length=200)),
            ],
        ),
    ]