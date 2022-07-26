# Generated by Django 4.0.6 on 2022-07-19 21:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0005_alter_snippet_code_alter_snippet_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField(
                    choices=[(1, 'Aggregator'), (2, 'Building Manager'),
                             (3, 'Aggregator And Building Manager')])),
                ('password', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
