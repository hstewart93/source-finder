# Generated by Django 3.0.3 on 2020-03-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("training", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="truesource",
            name="surface_brightness",
            field=models.FloatField(blank=True, null=True),
        )
    ]