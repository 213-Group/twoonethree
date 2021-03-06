# Generated by Django 2.2.4 on 2019-11-06 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mec', '0003_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='mo_h_dist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mo_h_dist', to='mec.District'),
        ),
        migrations.AddField(
            model_name='address',
            name='mo_s_dist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mo_s_dist', to='mec.District'),
        ),
        migrations.AddField(
            model_name='address',
            name='us_h_dist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='us_h_dist', to='mec.District'),
        ),
    ]
