# Generated by Django 4.1.3 on 2023-05-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Physical_AT_APP', '0002_physical_at_upload_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='physical_at_table',
            name='BTS_TYPE',
            field=models.CharField(default='2', max_length=100),
            preserve_default=False,
        ),
    ]
