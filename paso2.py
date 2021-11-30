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

