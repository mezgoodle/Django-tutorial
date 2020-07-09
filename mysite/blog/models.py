from django.db import models

class Task(models.Model):
    title = models.CharField('Title', max_length=50)
    task = models.TextField('Content')

    def __str__(self):
        return self.title
