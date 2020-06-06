from django.db import models
from django.contrib.auth.models import User



CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title