from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField()
    body  = models.TextField()
    date_added = models.DateTimeField(auto_now_add  = True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
