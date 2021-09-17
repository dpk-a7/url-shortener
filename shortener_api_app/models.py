from django.db import models

class req_URLS(models.Model):
    url = models.TextField()
    short_url = models.TextField()
    url_hit = models.IntegerField()
    posting_date = models.DateTimeField()

    def __str__(self):
        return self.url