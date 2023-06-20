from django.db import models

# Create your models here.
class IceCream(models.Model):
    name = models.CharField('Name', max_length=200)
    description = models.TextField('Discription')
    on_main = models.BooleanField('Go to the main page?', default=True)

    class Meta:        
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'