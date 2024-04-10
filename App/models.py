from django.db import models

# Create your models here.
class Fertilizer(models.Model):
    name = models.CharField(max_length=50, default='None')
    nitrogen = models.IntegerField()
    phosphorous = models.IntegerField()
    potassium = models.IntegerField()
    urea = models.IntegerField(default=0)
    DAP = models.IntegerField(default=0)
    muriate_of_potash = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', default='ok.jpg')
    desc = models.TextField(default='A')

    
    def __str__(self):
        return self.name

class Rates(models.Model):
    crop = models.ForeignKey('Fertilizer', on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.crop.name


class Crops(models.Model):
    name = models.CharField(max_length=255)
    fertilizer = models.ManyToManyField('Fertilizer', related_name='fertilizers')
    desc = models.TextField(default='A')

    def __str__(self):
        return self.name

class District_L(models.Model):
    name = models.CharField(max_length=50,default='a')
    summer = models.TextField(default='a')
    monsoon = models.TextField(default='a')
    post_monsoon = models.TextField(default='a')
    winter = models.TextField(default='a')
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    web  = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
