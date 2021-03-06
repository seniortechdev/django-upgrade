# Generated by Django 2.2.5 on 2020-02-24 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("onboarding", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Setting",
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
                ("timestamp", models.DateTimeField()),
                ("region_id", models.IntegerField(blank=True, null=True)),
                ("model_id", models.IntegerField(blank=True, null=True)),
                ("mail_count", models.IntegerField(blank=True, null=True)),
                ("pct_occ", models.IntegerField(blank=True, null=True)),
                ("pct_nocc", models.IntegerField(blank=True, null=True)),
                ("loo_min", models.IntegerField(blank=True, null=True)),
                ("sqft_min", models.IntegerField(blank=True, null=True)),
                ("sqft_max", models.IntegerField(blank=True, null=True)),
                ("equity_min", models.IntegerField(blank=True, null=True)),
                ("equity_max", models.IntegerField(blank=True, null=True)),
                ("tav_min", models.IntegerField(blank=True, null=True)),
                ("tav_max", models.IntegerField(blank=True, null=True)),
                ("tav_min_pctile", models.IntegerField(blank=True, null=True)),
                ("tav_max_pctile", models.IntegerField(blank=True, null=True)),
                ("est_val_min", models.IntegerField(blank=True, null=True)),
                ("est_val_max", models.IntegerField(blank=True, null=True)),
                ("est_val_min_pctile", models.IntegerField(blank=True, null=True)),
                ("est_val_max_pctile", models.IntegerField(blank=True, null=True)),
                ("mkt_val_min", models.IntegerField(blank=True, null=True)),
                ("mkt_val_max", models.IntegerField(blank=True, null=True)),
                (
                    "mosaic_filter",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("name_filter", models.IntegerField(blank=True, null=True)),
                ("append_phone", models.IntegerField(blank=True, null=True)),
                ("append_tax", models.IntegerField(blank=True, null=True)),
                ("append_parcel", models.IntegerField(blank=True, null=True)),
                ("sfr", models.IntegerField(blank=True, null=True)),
                ("mf", models.IntegerField(blank=True, null=True)),
                ("condo", models.IntegerField(blank=True, null=True)),
            ],
            options={"db_table": "audantic_region_settings", "managed": False,},
        ),
        migrations.DeleteModel(name="Settings",),
    ]
