# Generated by Django 2.0 on 2018-01-29 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_auto_20180130_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyingcourse',
            name='section',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]