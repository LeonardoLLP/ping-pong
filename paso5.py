#Nos disponemos a añadir las raquetas mediante dos variables

# pong_1_5.py: Clase RaquetaPong

import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
# Ancho de la ventana
VENTANA_HORI = 800 
# Alto de la ventana
VENTANA_VERT = 600  
# Fotogramas por segundo
FPS = 60  
# Color del fondo de la ventana (RGB)
BLANCO = (255, 255, 255)  

class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---
       
        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()
        
        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()
        
        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        
        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])
        
    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])

#Empezamos con la raqueta
class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()

        # --- Atributos de la Clase ---
        
        # Dimensiones de la Raqueta
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Raqueta
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2
        
        # Dirección de movimiento de la Raqueta
        self.dir_y = 0
        
    def mover(self):
        self.y += self.dir_y   
        
def main():
    # Inicialización de Pygame
    pygame.init()
    
    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 5")

    pelota = PelotaPong("bola_roja.png")

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho
