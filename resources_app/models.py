from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    affiliation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Journal(models.Model):
    name = models.CharField(max_length=255, unique=True)
    impact_factor = models.FloatField(null=True, blank=True)
    issn = models.CharField(max_length=9, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Publication(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    published_date = models.DateField()
    journal = models.ForeignKey(Journal, on_delete=models.SET_NULL, null=True, blank=True)
    volume = models.PositiveIntegerField(null=True, blank=True)
    issue = models.PositiveIntegerField(null=True, blank=True)
    pages = models.CharField(max_length=50, null=True, blank=True)
    doi = models.CharField(max_length=100, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class PubType(models.Model):
    publicationType = models.CharField(max_length=200)

    def __str__(self):
        return self.publicationType

class PaperTemp(models.Model):
    title = models.CharField(max_length=200)
    publicationType = models.ForeignKey(PubType, on_delete=models.CASCADE)
    content = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


