from django.db import models



class RegexQuery(models.Model):
    input_string = models.TextField()
    regex_pattern = models.CharField(max_length=255)
