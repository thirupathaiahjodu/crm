# Generated by Django 4.2.1 on 2023-06-01 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('crsid', models.IntegerField(primary_key=True, serialize=False)),
                ('crsname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='newstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile_Number', models.CharField(max_length=20)),
                ('Courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcube.enrollment')),
                ('Training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vcube.training')),
            ],
        ),
    ]