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
        
        