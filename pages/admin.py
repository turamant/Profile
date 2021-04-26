from django.contrib import admin

# Register your models here.
from pages.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','url','body')
    prepopulated_fields = {'url':('title',),}
