# Generated by Django 5.0.3 on 2024-08-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0033_alter_complaints_selfcomplaint_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='complainant_pacenumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
