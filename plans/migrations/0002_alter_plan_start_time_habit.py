# Generated by Django 4.0.5 on 2022-06-28 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('repeat', models.IntegerField(choices=[('week_days', (('7', 'saturday'), ('1', 'monday'), ('2', 'tuesday'), ('3', 'wednesday'), ('4', 'thursday'), ('5', 'friday'), ('6', 'sunday'))), ('x_day_week', (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'))), ('x_day_month', (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')))])),
                ('part_day', models.CharField(choices=[('anytime', 'anytime'), ('morning', 'morning'), ('afternoon', 'afternoon'), ('evening', 'evening')], max_length=9)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]