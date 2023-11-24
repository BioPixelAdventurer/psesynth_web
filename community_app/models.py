from django.db import models

# Create your models here.


class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll = models.ForeignKey('Roll', blank=True, null=True, on_delete=models.CASCADE)
    roll_s = models.ForeignKey('Roll_s', blank=True, null=True, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100, blank=True, null=True)
    field = models.ForeignKey('StudyField', on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    institution = models.ManyToManyField('Institution', blank=True, null=True)
    image = models.ImageField(upload_to='participants/', default='/defaults/default.png')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.institution.name})'


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

class StudyField(models.Model):
    field = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.field}'

class Institution(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Institutions'

class Roll(models.Model):
    roll = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.roll}'

class Roll_s(models.Model):
    roll = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.roll}'
