from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from PIL import Image


class UserManager(BaseUserManager):

    def create_user(self, username, first_name, password):
        user = self.model(
            username=username,
            first_name=first_name
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, password):
        user = self.create_user(username=username, first_name=first_name, password=password)
        user.is_staff = user.is_superuser = True
        user.save()
        return user



class User(AbstractBaseUser):

    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    second_name = models.CharField(max_length=150, default='', blank=True)
    image = models.ImageField(default='default.jpg')
    bio = models.CharField(max_length=500, default='', blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)




    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name',)


    objects = UserManager()





    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True


    # def save(self):
    #     super().save()

        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #     new_img = (300, 300)
        #     img.thumbnail(new_img)
        #     img.save(self.image.path)  











# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# @receiver(post_save, sender=User) # bu nima enandi?
# def create_blog_post_rus(sender, instance=None, created=False, **kwargs):
#     if created:

#         Account.objects.create(
#             user=instance
#         )
