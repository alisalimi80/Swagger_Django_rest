# Generated by Django 4.1.5 on 2023-01-04 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('time', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('country', models.CharField(max_length=120)),
                ('language', models.CharField(max_length=120)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.writers')),
            ],
        ),
    ]