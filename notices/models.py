from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title