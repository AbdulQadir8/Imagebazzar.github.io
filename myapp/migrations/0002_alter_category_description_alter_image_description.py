# Generated by Django 4.1.5 on 2023-01-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category", name="description", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="image", name="description", field=models.TextField(),
        ),
    ]
