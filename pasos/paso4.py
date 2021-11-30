import variables
import random

# Método reiniciar()
def reiniciar(self):
        self.x = variables.VENTANA_HORI / 2 - self.ancho / 2
        self.y = variables.VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])

#Método rebotar()
def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= variables.VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= variables.VENTANA_VERT:
            self.dir_y = -self.dir_y