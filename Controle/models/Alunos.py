from django.db import models

class User(models.Model):
    # Nome do usuário
    name = models.CharField(max_length=100)

    # Endereço de e-mail único do usuário
    email = models.EmailField(unique=True)