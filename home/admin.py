from django.contrib import admin
from home.models import Job, Category, Sub_Category
# Register your models here.
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Sub_Category)