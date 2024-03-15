from django.contrib import admin
from .models import Article,Category

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=("create_date","update_date")

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)