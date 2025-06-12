from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
    ('secretaire', 'Secrétariat'),
    ('chef_cabinet', 'Chef de Cabinet'),
    ('ministre', 'Ministre'),
    ('admin', 'Administrateur'),
)

class Utilisateur(AbstractUser):
    role = models.CharField(max_length=30, choices=ROLES, default='secretaire')
