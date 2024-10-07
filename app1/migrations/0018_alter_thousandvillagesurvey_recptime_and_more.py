# Generated by Django 4.2 on 2023-05-07 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_thousandvillagesurvey_recptime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thousandvillagesurvey',
            name='recptime',
            field=models.DateField(verbose_name='样本调查时间'),
        ),
        migrations.AlterField(
            model_name='thousandvillagesurvey',
            name='remark',
            field=models.TextField(max_length=1500, null=True, verbose_name='备注'),
        ),
    ]
