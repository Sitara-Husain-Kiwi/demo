# from django import forms
# from django.contrib import admin
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.core.exceptions import ValidationError

# from .models import MyUser

# class UserCreationForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = '__all__'


#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()
#     class Meta:
#         model = MyUser
#         fields = 'first_name','last_name','email', 'phone', 'is_admin'

# class UserAdmin(BaseUserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm

#     list_display = ('first_name','last_name','email', 'phone', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name','last_name','email', 'phone')}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('first_name','last_name','email', 'phone'),
#         }),
#     )
#     search_fields = ('username',)
#     ordering = ('username',)
#     filter_horizontal = ()

# admin.site.register(MyUser, UserAdmin)

# admin.site.unregister(Group)