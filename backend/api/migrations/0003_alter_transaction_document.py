# Generated by Django 4.0.1 on 2022-10-17 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_transaction_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='document',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.document'),
        ),
    ]
