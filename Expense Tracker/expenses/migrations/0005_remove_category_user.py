# Generated by Django 5.0.4 on 2024-10-23 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_alter_category_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]