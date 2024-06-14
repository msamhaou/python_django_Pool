from django.db import models

# Create your models here
class Author(models.Model):
    name = models.CharField(max_length=32, blank=False, unique=True)
    
    def __str__(self) -> str:
        return str(self.name)
    
class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        blank=False
    )
    title = models.CharField(max_length=32)
    def __str__(self) -> str:
        return str(self.title)
