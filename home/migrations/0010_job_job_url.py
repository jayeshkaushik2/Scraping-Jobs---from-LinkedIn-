# Generated by Django 3.2 on 2021-10-08 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_job_category_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_url',
            field=models.CharField(default=None, max_length=1000000, null=True),
        ),
    ]