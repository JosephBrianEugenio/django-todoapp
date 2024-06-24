from django.db import models

class Board(models.Model):
    board_name = models.CharField(max_length=255, null=True)
    class Meta:
        verbose_name_plural = "Boards"

    def __str__(self):
        return self.board_name
