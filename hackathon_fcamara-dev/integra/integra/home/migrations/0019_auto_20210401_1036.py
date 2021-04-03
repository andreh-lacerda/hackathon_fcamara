# Generated by Django 3.1.7 on 2021-04-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_profile_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemselection',
            name='item',
            field=models.CharField(choices=[('Agenda escolar', 'Agenda escolar'), ('Apontador com depósito', 'Apontador com depósito'), ('Borracha escolar', 'Borracha escolar'), ('Caderno brochurão - 80 fls', 'Caderno brochurão - 80 fls'), ('Caderno de desenho - 96 fls', 'Caderno de desenho - 96 fls'), ('Caderno universitário - 200 fls', 'Caderno universitário - 200 fls'), ('Calculadora de bolso 8 dígitos', 'Calculadora de bolso 8 dígitos'), ('Caneta esferográfica (2 azuis, 1 preta e 1 vermelha)', 'Caneta esferográfica (2 azuis, 1 preta e 1 vermelha)'), ('Canetinha hidrográfica (12 cores)', 'Canetinha hidrográfica (12 cores)'), ('Cola branca 90g', 'Cola branca 90g'), ('Cola colorida', 'Cola colorida'), ('Esquadro 45º', 'Esquadro 45º'), ('Esquadro 60º', 'Esquadro 60º'), ('Giz de cera (12 cores)', 'Giz de cera (12 cores)'), ('Grafite 0.7', 'Grafite 0.7'), ('Lápis de cor (12 cores)', 'Lápis de cor (12 cores)'), ('Lápis grafite', 'Lápis grafite'), ('Lapiseira 0.7', 'Lapiseira 0.7'), ('Massa para modelar', 'Massa para modelar'), ('Material dourado', 'Material dourado'), ('Pasta plástica transparente com elástico', 'Pasta plástica transparente com elástico'), ('Pincel nº 8', 'Pincel nº 8'), ('Régua', 'Régua'), ('Tesoura sem ponta', 'Tesoura sem ponta'), ('Tinta guache (6 cores)', 'Tinta guache (6 cores)'), ('Transferidor 180º', 'Transferidor 180º')], max_length=255, null=True),
        ),
    ]
