# Generated by Django 3.2 on 2021-10-08 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_job_from_cateogory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='from_cateogory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]
