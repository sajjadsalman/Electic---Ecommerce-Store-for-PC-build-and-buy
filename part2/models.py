from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=500)
    url = models.URLField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"name:{self.name}, url:{self.url}, description:{self.description}"
