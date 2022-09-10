# Generated by Django 4.0.5 on 2022-09-10 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_colour_tmp_portfolio_colour'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioColourAdapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('timestamp_colour_change', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='colourhistory',
            old_name='colour_hex_value',
            new_name='colour',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='portfoliocolouradapter',
            name='history_colour_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.colourhistory'),
        ),
    ]