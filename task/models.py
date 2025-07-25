from django.db import models


# Create your models here.

class Priority(models.TextChoices):
    HIGH = 'H','High'
    MEDIUM = 'M','Medium' 
    LOW = 'L', 'LOW'
    

class Category(models.TextChoices):
    TO_DO = 'TD','TO DO'
    Progress = 'IP','In Progress'    
    Completed = 'C','Completed'

class Tasks(models.Model):
    title = models.CharField(max_length = 100)
    due_date = models.DateField()
    category = models.CharField(max_length = 12, choices = Category.choices,default=Category.TO_DO)
    priority = models.CharField(max_length=6, choices = Priority.choices, default = Priority.LOW)
    added_on = models.DateTimeField(auto_now_add = True)
    
    
    
