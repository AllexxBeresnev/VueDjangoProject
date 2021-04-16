# Generated by Django 2.2.7 on 2021-04-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('course', models.CharField(max_length=140)),
                ('rating', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
