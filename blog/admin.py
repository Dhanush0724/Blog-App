from django.contrib import admin
from .models import PostModel
from .models import ProfileModel,Comment,savecon
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','date_create')


admin.site.register(PostModel, PostModelAdmin)

admin.site.register(ProfileModel)
admin.site.register(Comment)
admin.site.register(savecon)