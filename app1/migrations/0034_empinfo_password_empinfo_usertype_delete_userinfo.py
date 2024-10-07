# Generated by Django 4.2 on 2023-06-24 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0033_alter_userinfo_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='empinfo',
            name='password',
            field=models.CharField(default='123456', max_length=64, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='empinfo',
            name='usertype',
            field=models.IntegerField(choices=[(0, '超级用户'), (1, '普通用户')], default=1, verbose_name='用户类型'),
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
