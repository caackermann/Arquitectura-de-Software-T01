from django.db import models

# Create your models here.


class Message(models.Model):
    msg_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    client_ip = models.CharField(max_length=200, default='0')
    def __str__(self):
        return self.msg_text