# Generated by Django 4.1.7 on 2023-09-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_alter_book_page_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
