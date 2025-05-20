from django.db import models
import datetime
# Create your models here.
class Task(models.Model):
    description=models.TextField(max_length=30)
    date=models.DateField(default=datetime.date.today)
    is_completed=models.BooleanField(default=False)