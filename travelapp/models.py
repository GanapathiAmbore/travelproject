from django.db import models

class Destination(models.Model):
    name=models.CharField(max_length=10)
    img=models.ImageField()
    desc=models.TextField()
    offer=models.BooleanField(default=False)
    price=models.FloatField()

    def __str__(self):
        return self.name


