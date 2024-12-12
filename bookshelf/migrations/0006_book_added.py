# Generated by Django 3.2.4 on 2021-10-10 18:14

from django.db import migrations, models
from django.utils import timezone
from bookshelf.models import Book

class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0005_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Added',
            field=models.DateField(default=timezone.now),
        ),
    ]