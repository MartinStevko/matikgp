from django.db import models

class Druzinka(models.Model):
    nazov = models.CharField(max_length=100, unique=True)
    url_number = models.IntegerField(unique=True, null=True)

    def __str__(self):
        return "Družinka {}".format(self.nazov)

class Ucet(models.Model):
    idDruzinka = models.OneToOneField(Druzinka, on_delete=models.CASCADE, null=True)

    peniaze = models.IntegerField(default=1000)
    popularita = models.IntegerField(default=0)

    def __str__(self):
        return "Účet družinky {}".format(self.idDruzinka.nazov)

class Pokemon(models.Model):
    nazov = models.CharField(max_length=100)
    idDruzinka = models.ForeignKey(Druzinka, on_delete=models.CASCADE)

    sila = models.IntegerField(default=0)
    rychlost = models.IntegerField(default=0)
    postreh = models.IntegerField(default=0)
    odolnost = models.IntegerField(default=0)

    energia = models.IntegerField(default=10)
    jedol = models.BooleanField(default=False)

    def __str__(self):
        return "Pokémon {} družinky {}".format(self.nazov, self.idDruzinka.nazov)

class Trener(models.Model):
    meno = models.CharField(max_length=100)
    cena = models.IntegerField(default=0)
    vMeste = models.BooleanField(default=False)

    qSila = models.IntegerField(default=0)
    qRychlost = models.IntegerField(default=0)
    qPostreh = models.IntegerField(default=0)
    qOdolnost = models.IntegerField(default=0)

    def __str__(self):
        return "Tréner {}".format(self.meno)

class Kurz(models.Model):
    idTrener = models.ForeignKey(Trener, on_delete=models.CASCADE)
    idPokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return "Kurz cislo {}".format(self.id)

class Akcia(models.Model):
    meno = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.meno)
