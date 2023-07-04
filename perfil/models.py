from django.db import models


# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    essencial = models.BooleanField(default=False)
    valor_planejado = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.categoria


class Conta(models.Model):
    banco_choices = (
        ('NUBANK', 'NUBANK'),
        ('BANCO DO BRASIL', 'BANCO DO BRASIL'),
        ('ITAU', 'ITAU'),
        ('CAIXA', 'CAIXA'),
        ('SANTANDER', 'SANTANDER'),
        ('BRADESCO', 'BRADESCO'),
    )
    tipo_choices = (
        ('pf', 'Pessoa Física'),
        ('pj', 'Pessoa Jurídica'),
    )

    apelido = models.CharField(max_length=100)
    banco = models.CharField(max_length=100, choices=banco_choices)
    tipo = models.CharField(max_length=100, choices=tipo_choices)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    icone = models.ImageField(upload_to='icones', null=True, blank=True)

    def __str__(self):
        return self.apelido
