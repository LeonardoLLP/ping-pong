#Al paso 4 le añadimos lo siguiente:
#Definimos la clase RaquetaPong y sus atributos
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

#Para dibujar la imagen de la raqueta        
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_a
        self.ancho, self.alto = self.imagen.get_size()