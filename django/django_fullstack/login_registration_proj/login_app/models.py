from django.db import models
from django.contrib.auth.hashers import check_password
import re

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        # first name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"

        # last name
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"

        # email basic check
        EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "Invalid email format"
            
        # or this : if '@' not in postData['email']:
        #     errors['email'] = "Invalid email"

        # password length
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        # confirm password
        if postData['password'] != postData['confirm_password']:
            errors['confirm'] = "Passwords do not match"

        return errors

class User(models.Model):

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
