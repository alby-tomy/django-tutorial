from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    social_media_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
