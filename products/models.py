from django.db import models
from django.conf import settings

class Prouduct():
    title= models.CharField(max_length=50)
    seller= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/prodcuts', blank=True)

    def __str__(self):
        return self.title
