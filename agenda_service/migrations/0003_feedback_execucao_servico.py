# Generated by Django 4.2.3 on 2024-02-29 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda_service', '0002_remove_feedback_execucao_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='execucao_servico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agenda_service.execucaoservico'),
            preserve_default=False,
        ),
    ]