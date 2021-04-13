# Generated by Django 3.0.5 on 2020-06-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'role',
            },
        ),
    ]
