# Generated by Django 4.2.1 on 2023-06-05 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vcube', '0004_demoattended'),
    ]

    operations = [
        migrations.CreateModel(
            name='demos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sno', models.IntegerField()),
                ('Date', models.DateField()),
                ('Faculty', models.CharField(max_length=30)),
                ('Time', models.TimeField()),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcube.courses_name')),
                ('Training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcube.training')),
            ],
        ),
    ]
