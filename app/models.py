from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100)
    


    def __str__(self):
        return self.topic_name
    
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    #if we want to add another column we have provide it with default values
    #the below given column is added after performing migrtions
    #we edit the default value in admin page while adding new data
    email=models.EmailField(default='akhif@gmail.com')
    

    def __str__(self):
        return self.name

class AccessRecord(models.Model):

    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.author
    