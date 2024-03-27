from django.db import models

# Create your models here.

class Topic(models.Model):
    category=models.CharField(max_length=240,unique=True)


    def __str__ (self):
        return '{}'.format(self.category)

class Film(models.Model):
    title=models.CharField(max_length=250)
    actors=models.TextField()
    img = models.ImageField(upload_to='gallery')
    desc=models.TextField()
    date=models.DateField()
    category=models.ForeignKey(Topic,on_delete=models.CASCADE)
    url=models.URLField(max_length=120)
    review = models.CharField(max_length=140, default='SOME STRING')
    rating = models.IntegerField(default=1)



    def __str__ (self):
        return '{}'.format(self.title)

