# Generated by Django 3.1 on 2021-08-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookzipcode', '0011_auto_20210810_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookorder',
            name='how_would_you_like_your_carpet_to_be_cleaned',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='is_the_property_furnished_or_empty',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='most_of_our_customers_who_book_after_builders_cleaning_also_include',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='please_tell_us_about_your_place',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='we_recommend_a_total_of_time_served',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
