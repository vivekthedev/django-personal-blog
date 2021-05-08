from django.contrib import admin
from .models import Post, Comment
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', )
    # search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-publish',)


admin.site.register(Comment)
