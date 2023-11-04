from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.URLField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'