from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime

# Create your models here.
#title
#status
#date-current
#user
#priority

class TODO(models.Model):
    status_choices =  [
        ('C', 'COMPLETED'),
        ('P','PENDING')
        ]
    priority_choices =  [
        ('1', '1️⃣'),
        ('2','2️⃣'),
        ('3','3️⃣'),
        ('4','4️⃣'),
        ('5','5️⃣'),
        ('6','6️⃣'),
        ('7','7️⃣'),
        ('8','8️⃣'),
        ('9','9️⃣'),
        ('10','🔟'),
        ]    
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=2, choices=priority_choices)

    def __str__(self):
        return str(self.user)

class Contact(models.Model):
    contact_name = models.CharField(max_length=20)
    contact_email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return str(self.contact_email)