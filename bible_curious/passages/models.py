from django.db import models

# Create your models here.

class Collection(models.Model):
    """ Definition of shape of model."""
    name = models.CharField(max_length=50)
    
    def  __str__(self) -> str:
        return f"({self.id}) {self.name}"

    def calculate_href(self):
        return self.name.replace(" ", "_").lower()

class Story(models.Model):
    name = models.CharField(max_length=50)
    # Delete everything under the key first
    collection = models.ForeignKey(Collection, on_delete=models.RESTRICT)
    
    def  __str__(self) -> str:
        return f"({self.id}) {self.name}"
    
    def calculate_href(self):
        return f"{self.collection.name}/{self.name}".replace(" ", "_").lower()
    


    
    