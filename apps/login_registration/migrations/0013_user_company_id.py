# Generated by Django 2.2.5 on 2021-06-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0012_auto_20210628_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
