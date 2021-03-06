# Generated by Django 3.0.13 on 2021-04-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0052_auto_20210404_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='search_name',
            field=models.CharField(blank=True, db_index=True, help_text='A searchable name for the category, e.g. "Pokemon Emerald".', max_length=255, null=True),
        ),
    ]
