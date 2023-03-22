from django.db import models
from django.urls import reverse


class ToDo(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(default='', blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"pk": self.pk})
