from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager,PermissionsMixin
from rest_framework_jwt.settings import api_settings


class UserManger(BaseUserManager):
    def create_user(self ,email ,password=None,usertype='customer',**extra_fields):
        if not email:
            raise ValueError('email must be provided')
        email=self.normalize_email(email)
        user=self.model(email=email , user_type=usertype,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password,'super-admin',**extra_fields)



class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(unique=True)
    user_type= models.CharField(max_length=20 ,choices=[('super-admin', 'Super Admin'), ('staff', 'Staff'), ('customer', 'Customer')])
    is_staff= models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    objects =UserManger()
    USERNAME_FIELD= 'email'

class Profile(models.Model):
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)