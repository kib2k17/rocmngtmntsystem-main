# Generated by Django 5.1.1 on 2025-03-22 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0015_alter_complaints_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='date_endorse',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
