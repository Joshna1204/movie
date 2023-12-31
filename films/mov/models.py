from django.db import models

# Create your models here.
class Cards(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='mov/cards',blank=True,null=True)
    def __str__(self):
        return self.name



