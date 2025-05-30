# Generated by Django 5.0.4 on 2024-04-24 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0002_remove_denuncia_descricao_remove_denuncia_imagem"),
    ]

    operations = [
        migrations.AddField(
            model_name="denuncia",
            name="descricao",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="denuncia",
            name="imagem",
            field=models.ImageField(default=1, upload_to="denuncias/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="denuncia",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="denuncias",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
