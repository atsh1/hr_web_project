from django.contrib import admin
from .models import Department, Employee

# Customizing the Employee list view
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'is_active', 'hire_date')
    list_filter = ('is_active', 'department', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email')

# Register the models using the custom admin class
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)

