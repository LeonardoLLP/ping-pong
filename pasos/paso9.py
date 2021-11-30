# Pasos realizados en las clases/funciones correspondientes:

# Añadida puntuación a clase, paso2.py
# Añadido cambio de puntuación, paso3.py (añadiendo self.ancho, que por ahora parece ser que se había escapado, al menos hasta comprobación)
# Añdido color negro, variables.py

# Inicialización de la fuente

import pygame
import variables
import raquetas

fuente = pygame.font.Font(None, 60)


texto = f"{raquetas.pelota.puntuacion} : {raquetas.pelota.puntuacion_ia}"
letrero = fuente.render(texto, False, variables.NEGRO)
variables.ventana.blit(letrero, (variables.VENTANA_HORI / 2 - fuente.size(texto)[0] / 2, 50))