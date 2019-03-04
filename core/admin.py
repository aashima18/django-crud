from django.contrib import admin
from .models import Dept,Employee


admin.site.register(Dept)



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('dept','First_name','emp_desg')
    search_fields = ['First_name']
    
