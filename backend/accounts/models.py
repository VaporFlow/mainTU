from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Custom user model with role field."""

    class Role(models.TextChoices):
        PLANNER = "planner", "Planner"
        SUPERVISOR = "supervisor", "Supervisor"
        ADMIN = "admin", "Admin"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.PLANNER)

