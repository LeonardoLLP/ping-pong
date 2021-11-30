import variables
import pygame
import raquetas

# Método mover
def mover(self):
    self.y += self.dir_y
    if self.y <= 0:
        self.y = 0
    if self.y + self.alto >= variables.VENTANA_VERT:
        self.y = variables.VENTANA_VERT - self.alto

def check_status(self):
    for event in pygame.event.get():
        if event.type == QUIT:
            jugando = False

        # Detecta que se ha pulsado una tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                raqueta_1.dir_y = -5
            if event.key == pygame.K_s:
                raqueta_1.dir_y = 5

        # Detecta que se ha soltado la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                raqueta_1.dir_y = 0
            if event.key == pygame.K_s:
                raqueta_1.dir_y = 0