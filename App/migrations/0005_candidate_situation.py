# Generated by Django 4.2.1 on 2023-05-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0004_candidate_job"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="Situation",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Disapproved", "Disapproved"),
                ],
                default="Pending",
                max_length=50,
                null=True,
            ),
        ),
    ]
