from django.contrib import admin
from .models import Review, WatchList,StreamPlatform
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display=['watchlist','rating']


admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review,ReviewAdmin)