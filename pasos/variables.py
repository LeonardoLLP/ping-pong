import pygame

# Definición de constantes
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo

BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)
NEGRO = (0, 0, 0)  # Color del texto (RGB)

ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
pygame.display.set_caption("Pong 1")