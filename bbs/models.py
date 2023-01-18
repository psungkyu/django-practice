from django.db import models

# Create your models here.
class Article(models.Model):
    SEX_TYPES = (
        ('W', 'Woman'),
        ('M', "Man"),
    )
    content_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=80)
    created_by = models.CharField(max_length=1, choices=SEX_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
