# Generated by Django 4.1.7 on 2023-09-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
