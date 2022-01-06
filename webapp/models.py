from django.db import models

# Create your models here.
class Assignment(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    