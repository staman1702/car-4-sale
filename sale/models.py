from django.db import models
from django.contrib.auth.models import User
import datetime


STATUS = ((0, "Draft"), (1, "Published"))

today = datetime.datetime.now()
current_year = today.year

YEAR_CHOICES = [(year, str(year)) for year in range(1977, current_year)]

# Create your models here.


class CarMake(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.make} - {self.name}"

    class Meta:
        unique_together = ['make', 'name']
        ordering = ['make', 'name']  # Order by 'make' and then by 'name'


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sale_posts"
    )
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    production_year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=2022,
        verbose_name=("Production Year"),
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | posted by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
