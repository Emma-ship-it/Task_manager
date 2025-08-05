from django.db import models
from django.contrib.auth import get_user_model 
from django.utils import timezone

# Create your models here.
User = get_user_model()

class Priority(models.TextChoices):
    HIGH = 'H','High'
    MEDIUM = 'M','Medium' 
    LOW = 'L', 'Low'
    

class Category(models.TextChoices):
    TO_DO = 'TD','TO DO'
    Progress = 'IP','In Progress'    
    Completed = 'C','Completed'

class Tasks(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    category = models.CharField(max_length = 12, choices = Category.choices,default=Category.TO_DO)
    priority = models.CharField(max_length=6, choices = Priority.choices, default = Priority.LOW)
    added_on = models.DateTimeField(auto_now_add = True)
    added_by = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def due(self):
        today= timezone.now()
        return today > self.due_date
    
    
    
    
