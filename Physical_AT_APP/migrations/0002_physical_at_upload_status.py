# Generated by Django 4.1.3 on 2023-05-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Physical_AT_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Physical_At_upload_status',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Site_id', models.CharField(blank=True, max_length=100, null=True)),
                ('update_status', models.CharField(blank=True, max_length=100, null=True)),
                ('Remark', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
