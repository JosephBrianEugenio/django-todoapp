from django.db import models
from django.contrib.auth.models import User
class Board(models.Model):
    board_name = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Boards"

    def __str__(self):
        return self.board_name
