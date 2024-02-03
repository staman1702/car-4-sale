from django.contrib import admin
from .models import Post, CarMake, CarModel, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register()
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Comment)
