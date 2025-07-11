from django.db import models

class Review(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} - {self.date.strftime("%Y-%m-%d")}'
