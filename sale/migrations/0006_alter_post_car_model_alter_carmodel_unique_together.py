# Generated by Django 4.2.9 on 2024-02-03 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0005_alter_post_options_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='car_model',
            field=models.ForeignKey(limit_choices_to={'make': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.carmake')}, on_delete=django.db.models.deletion.CASCADE, to='sale.carmodel'),
        ),
        migrations.AlterUniqueTogether(
            name='carmodel',
            unique_together={('make', 'name')},
        ),
    ]