# Generated by Django 3.1 on 2021-08-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookzipcode', '0008_auto_20210810_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookorder',
            name='note',
        ),
        migrations.AddField(
            model_name='bookorder',
            name='user_description',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]