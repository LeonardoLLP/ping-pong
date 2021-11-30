import raquetas

#Al paso 7 debemos añadirle lo siguiente:
#Estrategia para mover la raqueta
def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3
        elif self.y < pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y

#Metodo para golpear la pelota
def golpear_ia(self, pelota):
        if (
            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self.ancho
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.ancho

#Para mover la raqueta y detectar el golpe de la pelota mediante un bucle principal
        raquetas.raqueta_1.mover()
        raquetas.raqueta_2.mover_ia(pelota)
        raquetas.raqueta_1.golpear(pelota)
        raquetas.raqueta_2.golpear_ia(pelota)
