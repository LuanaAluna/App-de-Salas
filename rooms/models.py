from django.db import models

class Bloco(models.Model):
    id= models.AutoField(primary_key=True)
    number_bloco = models.IntegerField(blank = True, null = True) #número do bloco

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    bloco = models.ForeignKey(
        Bloco, on_delete=models.PROTECT, related_name = 'room_bloco'
    ) #número do bloco
    number_room = models.IntegerField (blank = True, null = True) #número da sala
    capacity = models.IntegerField (blank = True, null = True) #capacidade maxima de pessoas na sala
    computers = models.IntegerField (blank = True, null = True) #quantidade de máquinas disponiveis 
    YES_OR_NO = {
        "S" : "SIM",
        "N" : "NÃO",
    }
    board = models.CharField(max_length=1, choices=YES_OR_NO,) #se há disponibilidade de quadro

    def __str__(self):
        return self.model
