# Generated by Django 4.0.6 on 2022-08-27 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departament_responsible', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='companies.company')),
            ],
        ),
    ]