# Generated by Django 4.2 on 2023-05-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_alter_thousandvillagesurvey_recptime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thousandvillagesurvey',
            name='remark',
            field=models.CharField(max_length=1500, null=True, verbose_name='描述(选填)'),
        ),
    ]
