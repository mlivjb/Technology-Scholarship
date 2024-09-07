from django.db import models
from django.utils.translation import gettext_lazy as _

class Map(models.Model):
    name = models.CharField(max_length=50)
    
    def  __str__(self) -> str:
        return f"({self.id}) {self.name}"
    
    def calculate_href(self):
        return f"{self.name}".replace(" ", "_").lower()
    
    
class FavouriteMap(models.Model):
    """Remember the users' favourite map"""
    user_sub = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=50, default="")
    def  __str__(self) -> str:
        return f"({self.user_sub}) {self.name}"
