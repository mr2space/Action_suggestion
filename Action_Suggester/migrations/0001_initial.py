# Generated by Django 5.2 on 2025-04-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueryLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_query', models.TextField()),
                ('tone', models.CharField(max_length=100)),
                ('intent', models.CharField(max_length=100)),
                ('suggested_action', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
