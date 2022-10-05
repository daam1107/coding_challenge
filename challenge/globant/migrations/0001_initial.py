# Generated by Django 4.1.1 on 2022-10-04 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hired_employees',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField()),
                ('department_id', models.IntegerField()),
                ('job_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='globant.hired_employees')),
                ('department', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='globant.hired_employees')),
                ('job', models.CharField(max_length=255)),
            ],
        ),
    ]