# Generated by Django 3.1.7 on 2021-04-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210409_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectureticket',
            name='cancel_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]