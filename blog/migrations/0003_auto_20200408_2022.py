# Generated by Django 3.0.4 on 2020-04-08 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cmmnt'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmmnt',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cmmnt',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]