from django.contrib import admin


# Register your models here.
from .models import SignUp, PersonalInfo


class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp
        
admin.site.register(SignUp, SignUpAdmin)


class PersonalInfoAdmin(admin.ModelAdmin):
    class Meta:
        model = PersonalInfo
        
admin.site.register(PersonalInfo, PersonalInfoAdmin)