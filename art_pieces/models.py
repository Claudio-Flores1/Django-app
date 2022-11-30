from django.db import models

# Create your models here.
class Art(models.Model):
    artist_name = models.CharField(max_length=100)
    piece_name = models.CharField(max_length=100, default='SOME STRING')
    year_made = models.CharField(max_length=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.artist_name} {self.year_made} {self.year_made}"

    def as_dict(self):
        return {
            'id': self.id,
            'artist': self.artist_name,
            'piece': self.piece_name,
            'year': self.year_made,
        }

class Museum(models.Model):
    museum_name = models.CharField(max_length=100)
    museum_location = models.CharField(max_length=100, default='SOME STRING')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.museum_name} is located in {self.museum_location}"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.artist_name,
            'location': self.piece_name,
        }