# Generated by Django 4.2.6 on 2023-10-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_category_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="categories",
            new_name="category",
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]