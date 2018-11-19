from django.contrib import admin

# Register your models here.
from .models import Post, Page
from django.db import models

# admin.site.register(Post)
admin.site.register(Page)

from markdownx.widgets import AdminMarkdownxWidget


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


admin.site.register(Post, MyModelAdmin)


# from markdownx.admin import MarkdownxModelAdmin
#
# admin.site.register(Post, MarkdownxModelAdmin)