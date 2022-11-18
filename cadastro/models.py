from django.db import models
import string
import random
# Create your models here.
class Usuario(models.Model):
        login = models.CharField(max_length=15)
        senha  = models.CharField(max_length=15, blank=True)
        
        data_nascimento = models.DateField(auto_now_add=False, auto_now=False)
        
        


        def __str__(self):
                return self.login
        
        if senha == '':
            abc = string.ascii_letters
            pontuacao = string.punctuation
            senha = abc + pontuacao
            ''.join(random.SystemRandom().choices(senha, k=15))