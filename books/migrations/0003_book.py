# Generated by Django 4.2.7 on 2023-11-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('publish_date', models.DateField()),
                ('average_rating', models.FloatField(default=0.0)),
                ('authors', models.ManyToManyField(to='books.author')),
                ('genres', models.ManyToManyField(to='books.genre')),
            ],
        ),
    ]