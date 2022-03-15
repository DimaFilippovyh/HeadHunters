from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    text = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Summary(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'summaries'

    def __str__(self):
        return f"{self.text[:50]}..."


class Vacancy(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return f"{self.text[:50]}..."