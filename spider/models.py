from django.db import models

class Bulletin(models.Model):
    source = models.CharField(max_length = 300)
    title = models.CharField(max_length = 50, blank=True)
    time = models.DateField(blank=True)
    content = models.CharField(max_length = 300, blank=True)

    def __str__(self):
        return self.title

