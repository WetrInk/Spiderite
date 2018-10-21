from django.db import models

class Bulletin(models.Model):
    source = models.CharField(max_length = 300)
    title = models.CharField(max_length = 50)
    time = models.CharField(max_length = 20)
    content = models.CharField(max_length = 300)

    def __str__(self):
        return self.title

