# Generated by Django 4.2.1 on 2023-06-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcube', '0009_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
