from statistics import mode
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Room Object

# Validate Room_Name


def validate_room_name(value):
    if ' ' in value:
        raise ValidationError("Room Name Should not have any white-spaces")
    else:
        return value


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(
        max_length=256, unique=True, validators=[validate_room_name])
    owner_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    room_desc = models.TextField()

    def __str__(self):
        return self.room_name
