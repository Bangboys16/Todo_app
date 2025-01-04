from django.db import models



class Task(models.Model):
    
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name