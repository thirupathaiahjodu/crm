# Generated by Django 4.2.1 on 2023-07-15 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vcube', '0017_delete_student_recent_placed_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='demodelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sno', models.IntegerField()),
                ('Date', models.DateField()),
                ('Faculty', models.CharField(max_length=30)),
                ('Time', models.TimeField()),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcube.courses_name')),
                ('Training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vcube.training')),
            ],
        ),
    ]