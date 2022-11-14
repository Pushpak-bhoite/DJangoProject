from django.contrib import admin
from enroll.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','emp_name','email','work')
