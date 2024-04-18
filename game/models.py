from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="game/media/", null=True, blank=True)
    text = models.TextField()
    price = models.FloatField()
    rate = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

