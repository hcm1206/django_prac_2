# Generated by Django 4.0.4 on 2024-05-23 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('border', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('border_id', models.IntegerField()),
                ('작성자', models.CharField(max_length=255)),
                ('작성일', models.DateTimeField()),
                ('내용', models.CharField(max_length=255)),
            ],
        ),
    ]
