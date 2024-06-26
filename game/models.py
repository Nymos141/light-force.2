from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="game/media/", null=True, blank=True)
    text = models.TextField()
    price = models.FloatField(blank=True)
    rate = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    objects = models.Manager()

    # create = models.

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-create_date"]

    def __str__(self):
        return self.title


class Feedback(models.Model):
    text = models.TextField(verbose_name="Комментарий")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  related_name="Feedbacks")
    object = models.Model

    def __str__(self):
        return self.text

class Category(models.Model):
    text = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.text

