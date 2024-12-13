from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ORGANIZER', 'Organisateur'),
        ('PARTICIPANT', 'Participant'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='PARTICIPANT')

    def register(self):
        self.save()

    def unregister(self):
        self.delete()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')

    def create_project(self):
        self.save()

    def edit_project(self, title=None, description=None):
        if title:
            self.title = title
        if description:
            self.description = description
        self.save()

    def delete_project(self):
        self.delete()

