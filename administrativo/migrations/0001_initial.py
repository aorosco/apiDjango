# Generated by Django 4.2.6 on 2023-10-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroEntradaSalida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.IntegerField()),
                ('ac_no', models.IntegerField()),
                ('numero', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('auto_assign', models.BooleanField()),
                ('date', models.DateField()),
                ('timetable', models.TimeField()),
                ('on_duty', models.TimeField()),
                ('off_duty', models.TimeField()),
                ('clock_in', models.TimeField()),
                ('clock_out', models.TimeField()),
            ],
        ),
    ]
