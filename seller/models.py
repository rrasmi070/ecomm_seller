from django.db import models


class Register(models.Model):
    F_name = models.CharField(max_length=20)
    L_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Phone = models.IntegerField()
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    Aadhar = models.FileField(upload_to='adhar/', max_length=100)
    GST = models.FileField(upload_to='GST/', max_length=100)
    PAN = models.FileField(upload_to='pan/', max_length=100)
    Passbook = models.FileField(upload_to='Account/', max_length=100)
    Account = models.IntegerField()
    Ifsc = models.CharField(max_length=100)
    
    def __str__(self):
        return self.F_name
        
# from __future__ import unicode_literals

# from django.db import models
# # from django.core.mail import send_mail
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager


# class Register(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     Phone = models.IntegerField()
#     Date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     Aadhar = models.FileField(upload_to='adhar/', max_length=100)
#     GST = models.FileField(upload_to='GST/', max_length=100)
#     PAN = models.FileField(upload_to='pan/', max_length=100)
#     Passbook = models.FileField(upload_to='Account/', max_length=100)
#     Account = models.IntegerField()
#     Ifsc = models.CharField(max_length=100)
#     is_active = models.BooleanField(_('active'), default=True)


#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_full_name(self):
#         '''
#         Returns the first_name plus the last_name, with a space in between.
#         '''
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.first_name

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     '''
    #     Sends an email to this User.
    #     '''
    #     send_mail(subject, message, from_email, [self.email], **kwargs)


