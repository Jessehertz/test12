from django.contrib import admin
from .models import MyModel
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    list_display = 'name','email','wechat','phone','message'


admin.site.register(MyModel,MyModelAdmin)
