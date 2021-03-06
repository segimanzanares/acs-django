from django.db import models

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    deleted_at = models.DateTimeField(auto_now=False, null=True)
    
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=255, null=True)
    last_login = models.DateTimeField(auto_now=False, null=True)
    created_at = models.DateTimeField(auto_now=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    deleted_at = models.DateTimeField(auto_now=False, null=True)
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def is_authenticated(self):
        return True;