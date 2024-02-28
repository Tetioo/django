from django.contrib import admin
from .models import Students
from .models import Teachers
from .models import parents
from .models import post

# Register your models here.
admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(parents)
admin.site.register(post)

# title
# description
# author
# createdat