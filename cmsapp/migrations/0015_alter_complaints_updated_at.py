# Generated by Django 5.1.1 on 2025-03-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0014_alter_complaints_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
