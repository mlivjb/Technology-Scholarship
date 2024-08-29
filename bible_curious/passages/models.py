from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Collection(models.Model):
    """ Definition of shape of model."""
    name = models.CharField(max_length=50)
    
    def  __str__(self) -> str:
        return f"({self.id}) {self.name}"

    def calculate_href(self):
        return self.name.replace(" ", "_").lower()


class Story(models.Model):
    """ Definition of shape of model for stories under collection."""
    name = models.CharField(max_length=50)
    # Delete everything under the key first
    collection = models.ForeignKey(Collection, on_delete=models.RESTRICT)
    
    def  __str__(self) -> str:
        return f"({self.id}) {self.name}"
    
    def calculate_href(self):
        return f"{self.collection.name}/{self.name}".replace(" ", "_").lower()


class Step(models.Model):
    """ Definition of shape of model for steps under stories under collection."""
    class Step_types(models.TextChoices):
        PASSAGE = "P", _('Passage')
        QUESTION = "Q", _('Question')
        GAME = "G", _('Game')

    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=1,
        choices = Step_types.choices,
        default = Step_types.PASSAGE
    )
    # Delete everything under the key first
    story = models.ForeignKey(Story, on_delete=models.RESTRICT)
    step_number = models.IntegerField(
        default=1
    )
    
    def  __str__(self) -> str:
        return f"({self.step_number}) {self.name} ({self.type})"
    
    def calculate_href(self):
        return f"{self.story.collection.name}/{self.story.name}/{self.step_number}".replace(" ", "_").lower()
    
class Verse(models.Model):
    """ Definition of model for verses of the week."""
    reading = models.CharField(max_length=50)
    verse = models.TextField()
    explanation = models.TextField()
    group = models.CharField(max_length=50)
    week = models.IntegerField()

    def  __str__(self) -> str:
        return f"({self.week}) {self.reading}"

class Personalisation(models.Model):
    user_id = models.CharField(max_length=100),
    current_story = models.CharField(max_length=50),
    current_step = models.IntegerField()
