from django.db import models
# Create your models here.

class Book(models.Model):
    Book_id = models.IntegerField()
    Book_name = models.CharField(max_length=100)
    Book_author = models.CharField(max_length=100)
    Book_publish_year = models.DateField()
    Book_price = models.FloatField() 