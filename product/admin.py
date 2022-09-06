from django.contrib import admin
from product.models import Product,MainCategory,SubCategory,AdsSettings

MAX_OBJECTS=1

# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','slug','created_date','updated_date']

@admin.register(MainCategory)
class AdminMainCategory(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SubCategory)
class AdminSubCategory(admin.ModelAdmin):
    list_display = ['name']

@admin.register(AdsSettings)
class AdminAdsSettings(admin.ModelAdmin):
    # list_display = ['name']

    def has_add_permission(self, request):
          if self.model.objects.count() >= MAX_OBJECTS:
               return False
          return super().has_add_permission(request)