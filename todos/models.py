from django.db import models
from datetime import date

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Título")
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=False, blank=False, verbose_name="Data de entrega")
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()