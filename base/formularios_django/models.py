from django.db import models

SEXO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('n', 'Neutro'),
)


class Cliente(models.Model):
    nome = models.CharField(max_length=40)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField(blank=True, null=True)
    altura = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.nome
