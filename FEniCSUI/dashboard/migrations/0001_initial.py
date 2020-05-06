# Generated by Django 3.0.6 on 2020-05-06 02:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Project name (do not use space)', max_length=30)),
                ('description', models.CharField(help_text='a short description of the project', max_length=200)),
            ],
        ),
    ]
