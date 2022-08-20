from django.contrib import admin
from .models import Contact, Detail, Exam, Degree, Appeared, Photo
# Register your models here.


admin.site.register(Detail)
admin.site.register(Contact)
admin.site.register(Degree)
admin.site.register(Exam)
admin.site.register(Appeared)
admin.site.register(Photo)