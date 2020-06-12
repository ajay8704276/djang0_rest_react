from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True, )
    description = models.TextField(max_length=400, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    published = models.DateField()
    cover = models.ImageField(upload_to='covers/', blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
