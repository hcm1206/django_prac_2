# Generated by Django 4.0.4 on 2024-05-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0002_remove_phonebook_작성자'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonebook',
            name='작성자',
            field=models.CharField(default='admin', max_length=50),
            preserve_default=False,
        ),
    ]
