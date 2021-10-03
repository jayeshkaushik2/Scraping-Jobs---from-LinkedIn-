from django.db import models

# Create your models here.
class Category(models.Model):
    job_category = models.CharField(max_length=10000)
    job_subcategory = models.CharField(max_length=1000000)

    def __str__(self):
        return self.job_category

class Job(models.Model):
    company = models.CharField(max_length=10000)
    job_position = models.CharField(max_length=10000)
    location = models.CharField(max_length=10000)

    def __str__(self):
        return self.company
