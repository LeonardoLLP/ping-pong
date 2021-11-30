# Método mover
def mover(self):
    self.y += self.dir_y
    if self.y <= 0:
        self.y = 0
    if self.y + self.alto >= VENTANA_VERT:
        self.y = VENTANA_VERT - self.alto

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