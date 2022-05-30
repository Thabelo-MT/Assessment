from django.db import models

# Create your models here.

class TicketLogger(models.model):
    Name= models.CharField(max_length=20)
    Last_Name= models.CharField(max_length=30)
    Email = models.EmailField(max_length=70,blank=True,unique=True)
    Date_Launched = models.DateField()
    
    def __str__(self):
        return self.Name + '' + self.Last_Name + '' + self.Email + '' + self.Date_Launched + '' 
    