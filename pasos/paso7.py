import raquetas

# Método golpear()
def golpear(self, pelota):
    if (
        pelota.x < self.x + self.ancho
        and pelota.x > self.x
        and pelota.y + pelota.alto > self.y
        and pelota.y < self.y + self.alto
    ):
        pelota.dir_x = -pelota.dir_x
        pelota.x = self.x + self.ancho

# Detectar el golpe de la pelota
raquetas.raqueta_1.golpear(raquetas.pelota)
