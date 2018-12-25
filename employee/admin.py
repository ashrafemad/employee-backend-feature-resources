from django.contrib import admin

from employee.models import Job, Employee, SalaryOthers


class SalaryInline(admin.TabularInline):
    model = SalaryOthers
    extra = 0


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'gender', 'age')
    inlines = (SalaryInline,)


admin.site.register(Job)
admin.site.register(Employee, EmployeeAdmin)
