# Generated by Django 4.2 on 2023-05-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_alter_thousandvillagesurvey_recptime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thousandvillagesurvey',
            name='entrepre',
            field=models.IntegerField(choices=[(0, '未创业'), (1, '创业')], verbose_name='是否创业'),
        ),
    ]
