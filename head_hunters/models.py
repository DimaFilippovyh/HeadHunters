from pytils.translit import slugify
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
        verbose_name="URL")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)


class Summary(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
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
