# Generated by Django 5.0.2 on 2024-02-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=220),
        ),
    ]
