from django.conf import settings
from django.db import models


class SocialLinks(models.Model):
    email = models.EmailField()
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    website = models.URLField()
    linkdin = models.URLField()
    fb = models.URLField()
    insta = models.URLField()


class Interests(models.Model):
    interest = models.CharField(max_length=80)


class WorkExperience(models.Model):
    company = models.CharField(max_length=120)
    role = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)


class Education(models.Model):
    institute = models.CharField(max_length=80)
    course_name = models.CharField(max_length=80)
    grade = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default=1, null=True,
                                on_delete=models.SET_NULL)
    profile_pic = models.URLField(null=True)
    name = models.CharField(max_length=80)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    gender = models.CharField(max_length=20)
    education = models.OneToOneField(
        Education, on_delete=models.CASCADE, null=True)
    work_experience = models.OneToOneField(
        WorkExperience, on_delete=models.CASCADE, null=True)
    interest = models.ManyToManyField(Interests, null=True)
    social_links = models.OneToOneField(
        SocialLinks, on_delete=models.CASCADE, null=True)
