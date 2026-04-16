

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/images", null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
    