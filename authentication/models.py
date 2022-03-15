# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# # Create your models here.
# class UserManager(BaseUserManager):
#     def create_user(self, first_name, middle_name, last_name, username, email, phone, password=None):
        
#         if not first_name:
#             raise ValueError('Users must have a first name address')
#         if not last_name:
#             raise ValueError('Users must have a last name address')
#         if not username:
#             raise ValueError('Users must have a username address')
#         if not email:
#             raise ValueError('User must have an email address')
#         if not phone:
#             raise ValueError('Users must have a username address')

#         user = self.model(
#             first_name=first_name,
#             middle_name=middle_name,
#             last_name=last_name,
#             username=username,
#             email=self.normalize_email(email),
#             phone=phone,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, first_name, middle_name, last_name, username, email, phone, password=None):
#         user = self.create_user(
#             first_name=first_name,
#             middle_name=middle_name,
#             last_name=last_name,
#             username=username,
#             email=email,
#             phone=phone,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class MyUser(AbstractBaseUser):
#     first_name=models.CharField(max_length=100)
#     middle_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     username=models.CharField(max_length=100,unique=True)
#     email=models.EmailField()
#     phone=models.CharField(max_length=10)
    
#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['first_name','last_name','email', 'phone']

#     def __str__(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

    