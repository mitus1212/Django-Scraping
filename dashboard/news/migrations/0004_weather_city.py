# Generated by Django 2.1.7 on 2019-09-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_weather_pressure'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='city',
            field=models.TextField(default='warsaw', editable=False),
        ),
    ]
