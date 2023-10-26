```python
from django.db import models

class Tweet(models.Model):
    tweet_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField()
    processed = models.BooleanField(default=False)

class ModelOutput(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    is_real = models.BooleanField()
    confidence = models.FloatField()

class AuditLog(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    action_taken = models.CharField(max_length=255)
    action_time = models.DateTimeField(auto_now_add=True)
    action_by = models.CharField(max_length=255)
```