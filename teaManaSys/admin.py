from django.contrib import admin

# Register your models here.
import models

admin.site.register(models.major)
admin.site.register(models.college)
admin.site.register(models.student)
admin.site.register(models.teacher)
admin.site.register(models.courses)
admin.site.register(models.grade)
admin.site.register(models.User)
admin.site.register(models.classList)