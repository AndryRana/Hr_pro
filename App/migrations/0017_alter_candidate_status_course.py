# Generated by Django 4.2.1 on 2023-06-01 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0016_alter_candidate_smoker"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="status_course",
            field=models.CharField(
                choices=[
                    ("", "Select your status"),
                    ("I'm studying", "I'm studying"),
                    ("I took a break", "I took a break"),
                    ("Completed", "Completed"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
