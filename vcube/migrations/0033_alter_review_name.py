# Generated by Django 4.2.1 on 2023-08-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcube', '0032_studentinquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]