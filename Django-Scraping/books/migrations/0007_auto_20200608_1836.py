# Generated by Django 2.1.7 on 2020-06-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='book',
            name='link',
            field=models.URLField(),
        ),
    ]