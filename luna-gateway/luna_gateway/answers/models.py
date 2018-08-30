from django.db import models
from core.models import Timestamp


# Create your models here.
class Answer(Timestamp):
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE)
    source_code = models.TextField()
    owned_by = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
    )
