# Generated by Django 4.1.3 on 2023-05-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Physical_AT_APP', '0007_physical_at_table_upload_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='physical_at_table',
            name='Current_PHY_Status',
            field=models.CharField(default='2', max_length=100),
            preserve_default=False,
        ),
    ]