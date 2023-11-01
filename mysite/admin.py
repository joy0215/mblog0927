from django.contrib import admin
from mysite.models import Minji , Product
# Register your models here.
class MinjiAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

admin.site.register(Minji,MinjiAdmin)
admin.site.register(Product)
