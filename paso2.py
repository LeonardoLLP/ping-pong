# Empezamos a definir  la pelota
# pong_1_2.py: Clase PelotaPong

import random
import pygame
from pygame.locals import QUIT

#Definimos las constantes para la inicialización de la superficie de dibujo
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
def main():
    # Inicialización de Pygame
    pygame.init()
    
    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 2")
    
    pelota = PelotaPong("bola_roja.png")
    
    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)




