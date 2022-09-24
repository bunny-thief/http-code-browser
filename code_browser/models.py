from django.db import models
from django.conf import settings


class ResponseCode(models.Model):
    response_code = models.CharField(max_length = 3)
    #response_str = str(response_code)
    description = models.TextField()
    URL = models.URLField()
    response_type = models.CharField(max_length = 20)

    def __str__(self):
        return self.response_code