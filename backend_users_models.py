from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    ROLES = (
        ('secretaire', 'Secrétariat'),
        ('chef_cabinet', 'Chef de Cabinet'),
        ('ministre', 'Ministre'),
        ('admin', 'Administrateur'),
    )
    role = models.CharField(max_length=30, choices=ROLES, default='secretaire')