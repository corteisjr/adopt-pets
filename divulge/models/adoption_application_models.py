from django.db import models
from divulge.models import Pet, User


class AdoptionApplication(models.Model):
    choices_status = (
        ("AG", "Aguardando aprovação"),
        ("AP", "Aprovado"),
        ("R", "Recusado"),
    )

    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField()
    status = models.CharField(max_length=2, choices=choices_status, default="AG")

    def __str__(self):
        return self.pet.name
