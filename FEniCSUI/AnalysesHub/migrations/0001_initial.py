# Generated by Django 3.0.6 on 2020-05-06 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisConfig',
            fields=[
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dashboard.projects')),
                ('mesh', models.TextField()),
                ('visualizationMesh', models.TextField()),
                ('config', models.TextField()),
                ('result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SolverProgress',
            fields=[
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dashboard.projects')),
                ('progress', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SolverResults',
            fields=[
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dashboard.projects')),
                ('result', models.TextField()),
            ],
        ),
    ]