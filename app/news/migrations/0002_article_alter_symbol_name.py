# Generated by Django 4.0.3 on 2022-04-06 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('guid', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=512)),
                ('link', models.CharField(max_length=256)),
                ('pubDate', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='symbol',
            name='name',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
