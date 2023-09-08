from django.db import models


class Post(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField()
    description = models.TextField(max_length=200, default="Description")

    def __str__(self):
        return self.title
