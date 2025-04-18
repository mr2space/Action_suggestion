from django.db import models



class QueryLog(models.Model):
    original_query = models.TextField()
    tone = models.CharField(max_length=100)
    intent = models.CharField(max_length=100)
    suggested_action = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
