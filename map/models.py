from django.db import models

# Create your models here.
class Map_location(models.Model):
    lat=models.DecimalField(max_digits=8, decimal_places=6, default=0,null=True,blank=True)
    lng=models.DecimalField(max_digits=8, decimal_places=6, default=0)
    activity_name= models.CharField(max_length=100 ,default=None,blank=True)
    locations_name=models.CharField(max_length=30,default=None,blank=True)
    user_count=models.IntegerField(default=0,blank=True)#عدد المستفيدين

    def __str__(self):
            return self.locations_name+ self.activity_name
