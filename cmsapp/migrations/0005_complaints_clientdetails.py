# Generated by Django 5.1.1 on 2024-12-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0004_complaints_endorseemp_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='clientdetails',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]