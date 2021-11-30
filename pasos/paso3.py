import variables

# Método rebotar()
def rebotar(self):
    if self.x <= -self.ancho:
        self.reiniciar()
        self.puntuacion_ia += 1
    if self.x + self.ancho >= variables.VENTANA_HORI:
        self.reiniciar()
        self.puntuacion += 1
    if self.y <= 0:
        self.dir_y = -self.dir_y
    if self.y + self.alto >= variables.VENTANA_VERT:
        self.dir_y = -self.dir_y