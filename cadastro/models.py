from django.db import models
import string as s; from random import SystemRandom as sr;


# Create your models here.



class Usuario(models.Model):
        login = models.CharField(max_length=15)
        senha  = models.CharField(max_length=15, blank=True)
        
        data_nascimento = models.DateField(auto_now_add=False, auto_now=False)
        
        


        def __str__(self):
                return self.login
        
        def save(self, *args, **kwargs):
                if not self.senha: 
                        self.senha = ''.join(sr().choices(s.ascii_letters + s.punctuation, k=15))
                return super().save(*args, **kwargs)