# Generated by Django 4.1.3 on 2023-05-24 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Physical_AT_APP', '0003_physical_at_table_bts_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='physical_at_table',
            name='PHYSICAL_AT_ACCEPTANCE_DATE',
            field=models.DateField(null=True),
        ),
    ]
