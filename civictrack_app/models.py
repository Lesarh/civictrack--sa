from django.db import models
from django.db import models


class Report(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='reports/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    SENDER_CHOICES = [
        ('User', 'User'),
        ('Admin', 'Admin'),
    ]

    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    text = models.TextField()
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES, default='User')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} comment on {self.report.title}"