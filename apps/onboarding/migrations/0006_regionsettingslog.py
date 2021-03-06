# Generated by Django 2.2.5 on 2021-01-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("onboarding", "0005_hasattribution"),
    ]

    operations = [
        migrations.CreateModel(
            name="RegionSettingsLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year_qtr", models.CharField(max_length=6)),
                ("region_id", models.IntegerField(blank=True, null=True)),
                ("region_settings_id", models.PositiveIntegerField()),
                ("model_id", models.IntegerField(blank=True, null=True)),
                ("dt_update", models.DateField(blank=True, null=True)),
            ],
            options={"db_table": "region_settings_log", "managed": False,},
        ),
    ]
