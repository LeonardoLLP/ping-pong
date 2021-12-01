# Ping Pong

Autores:  
[Ana López Paloma](https://github.com/Analopez90)  
[Paula Naranjo Borrallo](https://github.com/paulaanb)  
[Leonardo Luque Paganelli](https://github.com/LeonardoLLP)

## Historia de Pong  
Aunque desde la aparición de los ordenadores programables en los años 40 del siglo XX se han escrito programas que podían considerarse juegos, se suele considerar que el primer videojuego fue Computer Tennis. Este videojuego fue creado en 1958 para la exposición anual del Laboratorio Nacional de Brookhaven (EEUU) y simulaba un pista de tenis vista lateralmente. El juego se visualizaba en la pantalla de un osciloscopio y se convirtió en la mayor atracción de esa exposición. Aunque al año siguiente la exposición contó con una versión mejorada, tras ella el equipo se desmontó para reutilizar los componentes en el Laboratorio.

Bastante años después, en septiembre de 1972, se comercializó la primera videoconsola de la historia dirigida a los hogares, Magnavox Odyssey. Esta videoconsola se conectaba a una pantalla de televisor y uno de los juegos incluidos era Table Tennis. En este juego cada jugador controlaba una paleta que golpeaba una pelota. El mismo año, pero en noviembre, la compañía Atari comercializó Pong, una de las primeras máquinas de arcade, destinadas a lugares públicos.

### Pong, el videojuego

Con Pong, un juego trivial para los estándares actuales, empezaba la era moderna de los videojuegos. Pong es un juego de deportes en dos dimensiones que simula un tenis de mesa. El jugador controla en el juego una paleta moviéndola verticalmente en la parte izquierda de la pantalla, y puede competir tanto contra un oponente controlado por computadora, como con otro jugador humano que controla una segunda paleta en la parte opuesta. Los jugadores pueden usar las raquetas para pegarle a la pelota hacia un lado u otro. El objetivo consiste en que uno de los jugadores consiga más puntos que el oponente al finalizar el juego. Estos puntos se obtienen cuando el jugador adversario falla al devolver la pelota.

La palabra Pong es una marca registrada por Atari Interactive (aunque la patente del juego la tuvo la empresa de Magnavox Odyssey), pero la palabra genérica "pong" se usa para describir el género de videojuegos.

Por todo ello, cuando se aprende a programar videojuegos, es habitual comenzar programando un juego como Pong, por su sencillez y también como homenaje al gran clásico.

## Pygame

Pygame es un conjunto de módulos de Python que facilitan la creación de videojuegos. Pygame utiliza internamente la biblioteca SDL (Simple DirectMedia Layer), escrita principalmente en C.

Pygame se distribuye bajo la licencia libre LGPL, lo que permite utilizarla tanto en proyecto libres como comerciales.

Además de la Documentación oficial de pygame, en Internet se pueden encontrar sitios y libros dedicados a la introducción a la programación en general, o a la introducción a la programación de videojuegos en particular, mediante pygame.

Para la realización del juego Pong, iremos por fases, implementando en cada paso uno de los elementos del programa.

Paso 2: Clase PelotaPong
El primer elemento del juego que programaremos será la pelota. Para definir la pelota crearemos una clase a la que llamaremos PelotaPong. Las clases son propias de la programación orientada a objetos y permiten ampliar los tipos de datos del lenguaje. Una vez definida la clase, podemos crear tantas variables de esa clase como queramos (por ejemplo, una o varias pelotas, en el caso de que quisiéramos jugar con varias pelotas a la vez).

El siguiente programa dibuja una pelota cuadrada de color rojo en el centro de la ventana y la desplaza en línea recta en una de las cuatro direcciones diagonales. Cuando llega al borde de la ventana, la pelota deja de verse aunque sigue moviéndose indefinidamente en la misma dirección.

Para situar los objetos en la ventana pygame utiliza un sistema de coordenadas cartesianas en el que el origen se encuentran en la esquina superior izquierda de la ventana y en el que el eje vertical está dirigido hacia abajo. De esta manera, los valores de las coordenadas serán siempre positivos: cuanto mayor sea la coordenada x más a la derecha estará el objeto y cuanto mayor sea la coordenada y más hacia abajo estará el objeto. Si se asignan valores negativos o mayores que el tamaño de la ventana, no se produce ningún error, pero el objeto simplemente no se verá (dependiendo del tamaño que tenga y de los valores utilizados, el objeto puede verse parcialmente).

'''# pong_1_2.py: Clase PelotaPong

    import random
    import pygame
    from pygame.locals import QUIT

    # Constantes para la inicialización de la superficie de dibujo
    VENTANA_HORI = 800  # Ancho de la ventana
    VENTANA_VERT = 600  # Alto de la ventana
    FPS = 60  # Fotogramas por segundo
    BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


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

    pygame.quit()


    if __name__ == "__main__":
    main()'''

Las instrucciones añadidas con respecto al paso 1 son las siguientes:
'''#Importación de módulos
        import random
    #Importamos el módulo random, que utilizaremos en el programa.

    Clase PelotaPong
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
        self.y += self.dir_y'''
En la definición de una clase se definen los atributos y los métodos de la clase. Los atributos son variables que van asociadas automáticamente a los objetos. Los métodos son funciones que se pueden aplicar a los objetos. En la definición de la clase para hacer referencia a que los atributos son los del propio objeto se indica con self.

El método __init__() es la función que se ejecuta automáticamente cuando se cree un objeto de la clase. Por eso, aprovechamos este método para definir los atributos de la clase. En el caso de la pelota de este juego, sus atributos serán: la imagen que se muestra en la pantalla, su tamaño, la posición en la pantalla y la dirección del movimiento:
Todos los métodos incluyen el argumento self que hace referencia al propio objeto. En este caso, también añadimos el argumento imagen que indicará el camino hasta el fichero de imagen de la pelota:
    def __init__(self, imagen):
Un atributo de la clase será imagen, que cargará el fichero con la imagen:
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()
Otros dos atributos serán el ancho y alto de la imagen, ancho y alto que se obtienen a partir del atributo imagen con el método get_size():
        self.ancho, self.alto = self.imagen.get_size()
Dos atributos más serán la posición horizontal y vertical de la imagen, x e y. Inicialmente, queremos que la pelota se dibuje en el centro de la pantalla. Para ello, tenemos que tener en cuenta que cuando indicamos la posición de un objeto, estamos indicando la posición de la esquina superior izquierda de su imagen. Si el objeto es muy pequeño, no se notará la diferencia, pero lo mejor es tener en cuenta el ancho y alto del objeto, restando la mitad del tamaño del objeto a la posición del centro de la ventana.

    '''VENTANA_HORI / 2self.ancho / 2VENTANA_VERT / 2self.alto / 2
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2'''
Dos atributos más serán la dirección horizontal y vertical de movimiento de la imagen, dir_x y dir_y. Numéricamente, serán los píxeles que se desplazará la pelota cada vez que se redibuje la pantalla.Inicialmente, la pelota se desplazará 5px aleatoriamente hacia arriba (-5) o hacia abajo (5), hacia la izquierda (-5) o hacia la derecha (5):
     '''self.dir_x = random.choice([-5, 5])
       self.dir_y = random.choice([-5, 5])'''
El método mover() es la función que define cómo se mueve la pelota. En este caso, simplemente añadimos a las posiciones los valores de las direcciones. Este método sólo se ejecutará cuando la llamemos en el cuerpo del programa.
La imagen siguiente muestra tres posiciones sucesivas de la pelota. La pelota se desplaza cada vez dir_x unidades en horizontal y dir_y unidades en vertical.


    ''' dir_ydir_x(2)dir_ydir_x
        def mover(self):  
        self.x += self.dir_x
        self.y += self.dir_y'''
Creación de la pelota
Una vez definida una clase, en el cuerpo del programa podemos crear objetos (es decir, variables) de esa clase. En este caso, creamos la variable pelota de la clase PelotaPong. Esta variable automáticamente tendrá los atributos definidos en la clase (imagen, tamaño, posición, dirección) y se le podrán aplicar los métodos definidos en la clase (mover()). Al crear la variable le debemos indicar el fichero de imagen a utilizar, en este caso una imagen png.

    '''pelota = PelotaPong("bola_roja.png")'''
Mover la pelota
Para que la pelota se mueva y se dibuje en la pantalla, en el bucle principal del programa debemos:

Llamar al método mover(), para que se modifique la posición de la pelota (es decir sus atributos x e y):
    '''pelota.mover()'''
Dibujar la pelota en su posición en la ventana. Para ello recurrimos al método bit() del objeto ventana, indicando la imagen que queremos dibujar y su posición en la ventana:  
    ''' ventana.blit(pelota.imagen, (pelota.x, pelota.y))'''
    
    
Paso 5: Clase RaquetaPong
En este paso añadiremos las raquetas. Para ello definiremos una clase RaquetaPong, similar a PelotaPong y crearemos dos variables de esa clase.

    # pong_1_5.py: Clase RaquetaPong

    import random
    import pygame
    from pygame.locals import QUIT

    # Constantes para la inicialización de la superficie de dibujo
    VENTANA_HORI = 800  # Ancho de la ventana
    VENTANA_VERT = 600  # Alto de la ventana
    FPS = 60  # Fotogramas por segundo
    BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


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

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


    if __name__ == "__main__":
    main()

Las instrucciones añadidas con respecto al paso 4 son las siguientes:

    Clase RaquetaPong
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
La clase RaquetaPong es muy similar a la clase PelotaPong.

El método __init__() de la clase RaquetaPong es un poco más simple que el de la clase PelotaPong.
Las paletas utilizarán siempre la misma imagen, por lo que no incluiremos el camino al fichero como argumento de la clase.
    def __init__(self):
El atributo imagen cargará el fichero con la imagen:
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()
El ancho y alto de la imagen, ancho y alto se obtienen a partir del atributo imagen con el método get_size():
        self.ancho, self.alto = self.imagen.get_size()
Las posiciones iniciales horizontal y vertical de la imagen, x e y que asignemos en la definición de la clase no es realmente importante, ya que cuando creemos las raquetas deberemos situarlas en posiciones distintas cambiando estos valores. Para ahorrarnos instrucciones en el cuerpo del programa, estableceremos la posición vertical centrada en la ventana (que es común a ambas raquetas).
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2
Como la raqueta sólo se desplaza en vertical, únicamente necesitamos el atributo dir_y, que guardará la dirección vertical de movimiento de la imagen. Numéricamente, serán los píxeles que se desplazará la raqueta. Inicialmente, la raqueta estará inmóvil (0):
        self.dir_y = 0
El método mover() es la función que define cómo se mueve la raqueta. Aunque lo modificaremos en el paso siguiente, por el momento simplemente añadimos a la posición vertical el valor de la dirección vertical.
    def mover(self):
        self.y += self.dir_y
Crear las raquetas
Una vez definida la clase, en el cuerpo del programa podemos crear objetos (es decir, variables) de esa clase. En este caso, creamos dos variables raqueta_1 y raqueta_2 de la clase RaquetaPong y modificamos sus atributos x para situarlas en posiciones distintas. Concretamente, las situamos a 60px de los lados izquierdo y derecho.

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho
Dibujar las raquetas
Para ello recurrimos al método bit() del objeto ventana, indicando la imagen que queremos dibujar y su posición en la ventana:

        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))
        

Paso 8: Raqueta controlada por el ordenador
En este paso, añadiremos el control de la raqueta del jugador controlado por el propio programa.

Para ello, crearemos los método mover_raqueta_ia() y golpear_raqueta_ia() en la clase RaquetaPong y en el bucle principal llamaremos a estos métodos.

    # pong_1_8.py: Jugador controlado por el programa (IA)

    import random
    import pygame
    from pygame.locals import QUIT

    # Constantes para la inicialización de la superficie de dibujo
    VENTANA_HORI = 800  # Ancho de la ventana
    VENTANA_VERT = 600  # Alto de la ventana
    FPS = 60  # Fotogramas por segundo
    BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


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
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= VENTANA_VERT:
            self.y = VENTANA_VERT - self.alto

    def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3
        elif self.y < pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y

    def golpear(self, pelota):
        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho

    def golpear_ia(self, pelota):
        if (
            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self.ancho
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.ancho


    def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 8")

    pelota = PelotaPong("bola_roja.png")

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()
        raqueta_2.mover_ia(pelota)
        raqueta_1.golpear(pelota)
        raqueta_2.golpear_ia(pelota)

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

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

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


    if __name__ == "__main__":
    main()
    
Las instrucciones añadidas con respecto al paso 7 son las siguientes:

Método mover_ia()
El ordenador seguirá la siguiente estrategia para mover la raqueta.

líneas 77 a 78: Si la raqueta se encuentra por debajo de la pelota, la raqueta se desplazará hacia arriba (dando un valor negativo a dir_y).
líneas 79 a 80: Si la raqueta se encuentra por encima de la pelota, la raqueta se desplazará hacia abajo (dando un valor positivo a dir_y).
líneas 81 a 82: Si la raqueta está a la altura de la pelota, la raqueta se detendrá (dando un valor nulo a dir_y).
línea 76: como el método necesita conocer la posición de la pelota, incluimos la pelota como argumento del método.
     def mover_ia(self, pelota):
       if self.y > pelota.y:
        self.dir_y = -3
       elif self.y < pelota.y:
        self.dir_y = 3
       else:
        self.dir_y = 0

        self.y += self.dir_y
Método golpear_ia()
Este método es como el método golpear() del jugador humano, pero teniendo en cuenta que la pelota se acerca por el lado izquierdo de la raqueta en vez de por el derecho.

    def golpear_ia(self, pelota):
        if (
            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self.ancho
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.ancho
Mover la raqueta y detectar el golpe de la pelota
Añadimos en el bucle principal del programa las llamadas a los métodos mover_ia() y golpear_ia() de la raqueta del jugador controlado por el propio programa (líneas 129 y 131).

        raqueta_1.mover()
        raqueta_2.mover_ia(pelota)
        raqueta_1.golpear(pelota)
        raqueta_2.golpear_ia(pelota)
