from django.contrib import admin

from models_demos.web.models import Employee, NullBlankDemo, Department, Project, Category


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'level')
    list_filter = ('level', 'works_full_time')
    search_fields = ('first_name', 'last_name')
    fieldsets = (('Personal info',
                  {'fields': ('first_name', 'last_name', 'age')}),
                 ('Professional info',
                  {'fields': ('level', 'years_of_experience')}),
                 ('Company Info',
                  {'fields': ('department', 'works_full_time', 'start_date')})
                 )


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
