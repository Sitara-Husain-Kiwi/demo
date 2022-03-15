from django.db import models

# Create your models here.
class AddBookModel(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    price=models.IntegerField()

    def __str__(self):
        return self.name