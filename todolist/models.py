from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import pre_save
from utils.unique_slug import unique_slug_generator


class Goal(models.Model):
    STATUS_CHOICES = [
        (0, 'doing'),
        (1, 'Done'),
        (2, 'Wasted'),
    ]
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True,
                            unique=True, allow_unicode=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    abstract = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purpose = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("goal", kwargs={'slug': self.slug})


class Work(models.Model):
    STATUS_CHOICES = [
        (0, 'doing'),
        (1, 'Done'),
        (2, 'Wasted'),
    ]
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True,
                            unique=True, allow_unicode=True)
    status = models.IntegerField(choices=STATUS_CHOICES,default=STATUS_CHOICES[0][0])
    abstract = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purpose = models.ManyToManyField(
        Goal, related_name='work_goals', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("work", kwargs={'slug': self.slug})


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance=instance)


pre_save.connect(slug_generator, sender=Work)
pre_save.connect(slug_generator, sender=Goal)
