import variables

# Método rebotar()
def rebotar(self):
    if self.x <= 0:
        self.dir_x = -self.dir_x
    if self.x + self.ancho >= variables.VENTANA_HORI:
        self.dir_x = -self.dir_x
    if self.y <= 0:
        self.dir_y = -self.dir_y
    if self.y + self.alto >= variables.VENTANA_VERT:
        self.dir_y = -self.dir_y