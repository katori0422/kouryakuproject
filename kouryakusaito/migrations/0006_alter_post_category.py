# Generated by Django 5.1.2 on 2024-11-26 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kouryakusaito', '0005_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('character', 'キャラクター'), ('enemy', '敵'), ('item', 'アイテム')], max_length=10),
        ),
    ]