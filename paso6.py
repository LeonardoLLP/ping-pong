# Método mover
def mover(self):
    self.y += self.dir_y
    if self.y <= 0:
        self.y = 0
    if self.y + self.alto >= VENTANA_VERT:
        self.y = VENTANA_VERT - self.alto