# Generated by Django 4.2.5 on 2023-10-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('dateOfBirth', models.DateField()),
                ('nationality', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
            ],
        ),
    ]
