# Generated by Django 5.1.2 on 2024-11-25 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kouryakusaito', '0002_post_kouryakupost_author_alter_kouryakupost_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kouryakupost',
            name='author',
        ),
    ]