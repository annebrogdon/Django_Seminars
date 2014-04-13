"""this is a docstring """
if __name__ == '__main__':

    from django.contrib import admin

    # Register your models here.
    from .models import SignUp
    class SignUpAdmin(admin.ModelAdmin):
        class Meta:
            model = SignUp
        
    admin.site.register(SignUp, SignUpAdmin)