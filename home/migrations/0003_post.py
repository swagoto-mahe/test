# Generated by Django 3.1 on 2021-07-29 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('wellcome_msg', models.CharField(blank=True, max_length=200)),
                ('wellcome_msg2', models.CharField(blank=True, max_length=200)),
                ('wellcome_msg3', models.TextField(blank=True)),
                ('best_team', models.CharField(blank=True, max_length=200)),
                ('commercial_cleaning', models.TextField(blank=True)),
                ('commercial_description', models.TextField(blank=True)),
                ('commercial_image', models.ImageField(blank=True, upload_to='')),
                ('dom_residentiam_clean', models.TextField(blank=True)),
                ('dom_residentiam_description', models.TextField(blank=True)),
                ('dom_residentiam_image', models.ImageField(blank=True, upload_to='')),
                ('cleaning_services', models.CharField(blank=True, max_length=200)),
                ('maintenance_services', models.TextField(blank=True)),
                ('maintenance_image', models.TextField(blank=True)),
                ('maintenance_description', models.TextField(blank=True)),
                ('covid_disinfection', models.TextField(blank=True)),
                ('covid_image', models.TextField(blank=True)),
                ('covid_description', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('what_makes_your_service', models.CharField(blank=True, max_length=200)),
                ('what_make_image', models.ImageField(blank=True, upload_to='')),
                ('what_make_li_1', models.CharField(blank=True, max_length=200)),
                ('what_make_li_2', models.CharField(blank=True, max_length=200)),
                ('what_make_li_3', models.CharField(blank=True, max_length=200)),
                ('what_make_li_4', models.CharField(blank=True, max_length=200)),
                ('what_make_li_5', models.CharField(blank=True, max_length=200)),
                ('what_make_li_6', models.CharField(blank=True, max_length=200)),
                ('what_make_li_7', models.CharField(blank=True, max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
