from django.contrib import admin
from .models import Post, CarMake, CarModel, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Comment)
