from django.contrib import admin
from .models import School,Student
# Register your models here.
class SchoolAdmin(admin.ModelAdmin):

    fields = ['name', 'principal', 'location']

    search_fields = ['name', 'location']

    list_filter = ['location']

    list_display = ['name', 'location', 'principal']

    list_editable = ['principal']

class StudentAdmin(admin.ModelAdmin):

        fields = ['name', 'age', 'school']

        search_fields = ['name']

        list_filter = ['age']

        list_display = ['name', 'age', 'school']

        list_editable = ['age']

admin.site.register(School,SchoolAdmin)
admin.site.register(Student,StudentAdmin)
