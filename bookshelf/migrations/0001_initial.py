# Generated by Django 4.2.17 on 2024-12-11 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Surname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TagName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Tag_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.book')),
                ('Tag_Key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.tags')),
            ],
        ),
        migrations.CreateModel(
            name='Book_Author_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author_Key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.authors')),
                ('Book_Key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.book')),
            ],
        ),
    ]
