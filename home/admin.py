from django.contrib import admin

from .models import Category,Article
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'status', 'cat_id']
  prepopulated_fields = {'slug':('cat_name',)}
  class Meta:
    model = Category

admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
  search_fields = ['art_name', 'description']
  list_display = ['__str__', 'cat_id', 'status', 'art_mo_ta', 'art_id']
  list_editable = ['cat_id', 'status', 'art_mo_ta']
  list_filter = ['cat_id', 'status']
  prepopulated_fields = {'art_slug':('art_name',)}
  class Meta:
    model = Article

admin.site.register(Article,ArticleAdmin)