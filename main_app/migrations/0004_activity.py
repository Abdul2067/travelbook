# Generated by Django 3.2.7 on 2021-11-29 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_travel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=100)),
                ('rating', models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], default=0, max_length=1)),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.travel')),
            ],
        ),
    ]
