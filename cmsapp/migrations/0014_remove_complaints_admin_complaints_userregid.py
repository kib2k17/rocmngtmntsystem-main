# Generated by Django 5.0.4 on 2024-04-30 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0013_rename_comp_id_complaintremark_comp_id_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints',
            name='admin',
        ),
        migrations.AddField(
            model_name='complaints',
            name='userregid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmsapp.userreg'),
        ),
    ]
