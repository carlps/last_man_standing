# Generated by Django 2.0.8 on 2018-09-03 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0005_auto_20180903_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nflteam',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nfl.Season'),
        ),
    ]
