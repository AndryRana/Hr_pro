# Generated by Django 4.2.1 on 2023-05-31 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0014_rename_travel_candidate_travel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="job",
            field=models.CharField(max_length=5, verbose_name="Job code"),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="message",
            field=models.TextField(verbose_name="Presentation"),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="salary",
            field=models.CharField(max_length=50, verbose_name="Salary expectation"),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="smoker",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], default="", max_length=10
            ),
        ),
    ]