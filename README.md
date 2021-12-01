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

Paso 1: Ventana de juego

El juego se ejecutará en una ventana independiente. Para crear la ventana, necesitamos bastante código específico de pygame, que no es necesario conocer de memoria, ya que lo podemos reutilizar de un proyecto a otro.

El siguiente programa genera una ventana en blanco con el título del juego, similar a la captura siguiente (la ventana está recortada en la captura).

    '''Pygame - Pong 1

    # pong_1_1.py: Ventana de juego

    import pygame
    from pygame.locals import QUIT

    # Constantes para la inicialización de la superficie de dibujo
    VENTANA_HORI = 800  # Ancho de la ventana
    VENTANA_VERT = 600  # Alto de la ventana
    FPS = 60  # Fotogramas por segundo
    BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


    def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 1")

    # Bucle principal
    jugando = True
    while jugando:
        ventana.fill(BLANCO)

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


    if __name__ == "__main__":
    main()


Cada una de las instrucciones tiene una función específica, que se comenta a continuación:

    '''Importación de módulos
    import pygame
    from pygame.locals import *
    #Importamos los módulos pygame. Para que al hacer referencia en el programa a las constantes de pygame no tengamos que incluir el nombre del módulo, las            importamos todas del módulo pygame.locals.

    #Definición de constantes
    # Constantes para la inicialización de la superficie de dibujo
    VENTANA_HORI = 800  # Ancho de la ventana
    VENTANA_VERT = 600  # Alto de la ventana
    FPS = 60  # Fotogramas por segundo
    BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)

Python no tiene un tipo de dato "constante" (es decir, un valor que no se pueda modificar). La costumbre, heredada de otros lenguajes, es simplemente escribir  el nombre de una variable en mayúsculas para indicar a quien lea nuestro código fuente que esa variable no se va a modificar en ningún momento del programa.   
Definimos así varias constantes:

El tamaño de la ventana de juego (en este caso, 800 x 600 px, la llamada resolución SVGA original).
Normalmente FPS hace referencia al número de veces por segundo que se actualiza la imagen en la ventana. En principio, cuanto más alto es ese valor, mejor se verán los objetos en movimiento, aunque cada pantalla admite un valor máximo y dependiendo de la complejidad de la creación de la imagen puede que no se puedan alcanzar valores muy altos. En pygame, la ventana se está actualizando constantemente y en cada actualización los objetos se desplazan, por lo que si la ventana se actualiza demasiadas veces, los objetos se desplazarán demasiado rápido. Para evitarlo, en pygame FPS significa el número máximo de veces que queremos que se actualice la ventana, aunque si debido a la complejidad de la imagen el número de veces que se actualiza la imagen es inferior, pygame no podrá alcanzarlo.
En pygame los colores se indican mediante códigos RGB, así que definimos una constante con el nombre del color para facilitar su referencia.
Inicialización

    '''# Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 1")
Con estas instrucciones:

Inicializamos pygame.
Creamos el objeto ventana que nos permite acceder al contenido de la ventana (al crearlo, le indicamos su tamaño).
Le damos un título a la ventana.
    
    '''Bucle principal
    # Bucle principal
    jugando = True
    while jugando:
        ventana.fill(BLANCO)

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()
El bucle principal se ejecuta continuamente:

línea 22: La variable lógica jugando controlará la repetición del bucle. Inicialmente, la variable tiene el valor True.
línea 23: Mientras se mantenga ese valor, el bucle se repetirá.
línea 24: En cada iteración pintamos la pantalla de blanco para borrar los elementos de la imagen anterior (en este programa todavía no ha elementos, pero podemos añadir ya esta instrucción).
líneas 26 a 28: Las pulsaciones de tecla o del ratón se reciben en forma de eventos.
línea 26: El bucle for recorre en cada iteración los eventos recibidos
línea 27: Si el evento es de tipo QUIT (es decir, que se ha cerrado la ventana del juego) ...
línea 28: La variable jugando pasa a False, por lo que el bucle while no se volverá a ejecutar.
línea 30: Todos los elementos de la pantalla se vuelven a dibujar (en este programa todavía no ha elementos, pero podemos añadir ya esta instrucción).
línea 31: Con esta instrucción pygame comprueba que la ejecución se mantiene en el número de FPS y no va demasiado rápida.
línea 33: Si hemos salido del bucle es que se ha cerrado la ventana, así que con esta instrucción le pedimos a pygame que cierre todos sus procesos.

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
    
Paso 3: Rebote de la pelota
En este paso mejoraremos el comportamiento de la pelota haciendo que la pelota rebote al chocar con los cuatro lados de la ventana. Para ello, añadiremos un nuevo método a la clase (rebotar()) que utilizaremos en el bucle principal del programa.

    '''# pong_1_3.py: Rebote de la pelota

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
        if self.x <= 0:
            self.dir_x = -self.dir_x
        if self.x + self.ancho >= VENTANA_HORI:
            self.dir_x = -self.dir_x
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y


    def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 3")

    pelota = PelotaPong("bola_roja.png")

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


    if __name__ == "__main__":
    main()

Las instrucciones añadidas con respecto al paso 2 son las siguientes:

Método rebotar():
Para conseguir que la pelota rebote contra las paredes, basta con detectar cuando la pelota llega al borde de la ventana y en ese momento cambiar la dirección del movimiento.

Al comprobar si se ha llegado al borde, es mejor hacer las comparaciones utilizando desigualdades (> o <) en vez de igualdades (==), ya que la pelota se desplaza varios píxeles a cada paso y podría saltarse el valor límite. Al escribir desigualdades, nos aseguramos de que detectamos si se supera el valor límite.
Como se ha comentado al colocar la pelota en el centro de la pantalla, la posición de un objeto corresponde a la posición de la esquina superior izquierda de la imagen. Por ello no es lo mismo detectar que se ha llegado al lado izquierdo de la ventana que al derecho. En el lado izquierdo podemos comparar la posición con el valor límite (0), pero en el lado derecho tenemos que tener en cuenta el ancho de la pelota. Ocurre lo mismo en vertical, puesto que abajo hay que tener en cuenta el alto de la pelota.
Cuando se choca con los lados derecho e izquierdo, sólo hay que cambiar la dirección horizontal de movimiento, mientras que cuando se choca con los lados de arriba y de abajo, sólo hay que cambiar la dirección vertical.
    
    self.x < 0
    self.y < 0
    self.y + self.alto > VENTANA_VERT
    self.x + self.ancho > VENTANA_HORI

    def rebotar(self):
        if self.x <= 0:
            self.dir_x = -self.dir_x
        if self.x + self.ancho >= VENTANA_HORI:
            self.dir_x = -self.dir_x
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

Comprobación del rebote:
Para que el programa compruebe si se debe producir un rebote basta con llamar al método en el bucle principal del programa:

    pelota.rebotar()
    
Paso 4: Reiniciar pelota al salir por los lados izquierdo y derecho
Realmente, en el juego de Pong la pelota no debe rebotar en todos los lados, como hacía en el programa anterior. Únicamente debe rebotar arriba y abajo. Si la pelota llega a alguno de los lados, significará que uno de los jugadores no ha devuelto la pelota. En ese caso, el jugador habrá perdido un punto y la pelota debe volver a lanzarse desde el centro (en dirección al jugador que ha ganado el punto, por ejemplo).

En este paso, modificaremos el método rebotar() y añadiremos un método reiniciar() para conseguir el comportamiento comentado en el párrafo anterior.

    # pong_1_4.py: Reiniciar pelota al salir por los lados

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


    def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 4")

    pelota = PelotaPong("bola_roja.png")

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


    if __name__ == "__main__":
    main()


Las instrucciones añadidas con respecto al paso 3 son las siguientes:

Método reiniciar():
Cuando la pelota se salga por los lados izquierdo y derecho, debe volver al centro, moviéndose en dirección contraria a la que tenía antes. para ello creamos un método reiniciar() que modifica los atributos de posición y dirección de movimiento.

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])
Método rebotar():
Modificamos el método rebotar(), de manera que cuando detecte que la pelota ha salido por los lados derecho e izquierdo, llame al método reiniciar().

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y
    
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
        
Paso 6: Mover raqueta con teclado
En este paso, añadiremos el movimiento de la raqueta del jugador humano.

El jugador humano va a controlar su raqueta (por ejemplo, la raqueta raqueta_1) mediante el teclado, concretamente la raqueta subirá al pulsar la tecla "w" y la raqueta "bajará" al pulsar la tecla "s". Para ello, no es necesario modificar la clase, pero en el bucle principal del programa tenemos que detectar la pulsación (y liberación) de las teclas y modificiar el atributo de dirección del movimiento.

    # pong_1_6.py: Mover raqueta con teclado

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


    def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 6")

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


Las instrucciones añadidas con respecto al paso 5 son las siguientes:

Mover la raqueta
Añadimos en el bucle principal del programa la llamada al método mover() de la raqueta.
        
        raqueta_1.mover()

Ahora que la raqueta se mueve, debemos impedir que se salga de la ventana. Para añadiremos en el método mover() dos condiciones que detecten si la raqueta se está saliendo (por arriba o por abajo).
    
    def mover(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= VENTANA_VERT:
            self.y = VENTANA_VERT - self.alto
            
Detectar las pulsaciones de teclado
Para pygame, las pulsaciones de teclado son eventos. Cuando se pulsa una tecla, pygame crea un evento pygame.KEYDOWN y guarda la tecla pulsada en event.key. Cuando se libera una tecla, pygame crea un evento pygame.KEYUP y guarda la tecla pulsada en event.key. Por ello, en el bucle for que recorre los eventos detectados añadiremos la comprobación de los eventos y la modificación del atributo dir_y de dirección del movimiento.

línea 99-100: Si se ha pulsado la tecla "w", daremos un valor negativo (por ejemplo, -5) al atributo dir_y, para que la raqueta se desplace hacia arriba.
línea 101-102: Si se ha pulsado la tecla "s", daremos un valor positivo (por ejemplo, 5) al atributo dir_y, para que la raqueta se desplace hacia abajo.
líneas 106-109: Si se libewran las teclas "s" y "w", daremos un valor nulo (0) al atributo dir_y, para detener la raqueta.
            
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
                    
Paso 7: Golpear la pelota con la raqueta

En este paso, añadiremos el golpe de la raqueta del jugador humano a la pelota.

Para ello, crearemos el método golpear_raqueta() en la clase RaquetaPong y en el bucle principal llamaremos al método.

    # pong_1_7.py: Golpe raqueta jugador humano

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

    def golpear(self, pelota):
        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho


    def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 7")

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
        raqueta_1.golpear(pelota)

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


Las instrucciones añadidas con respecto al paso 6 son las siguientes:

Método golpear()
Este golpe es quizás el punto más complicado del programa.

líneas 78 a 18: En principio, el golpe se produce cuando la raqueta y la pelota están en contacto y el resultado del golpe es que la pelota debe cambiar de dirección de movimiento horizontal.

    pelota.x < self.x + self.ancho
    pelota.y + pelota.alto > self.y
    pelota.x < self.x + self.ancho
    pelota.y < self.y + self.alto

líneas 83 y 84: Para evitar que el programa detecte colisión en dos o más iteraciones consecutivas (lo que provocaría cambios continuos de dirección, es decir, el zigzazeo de la pelota), además de cambiar la dirección de movimiento de la pelota, desplazaremos explícitamente la pelota fuera de la raqueta.
Un detalle que no tiene en cuenta el programa es cuando la raqueta golpea verticalmente la pelota, es decir, cuando la golpea desde abajo o desde arriba cuando está pasando. Tal y como está redactado el programa, este golpe produce la devolución de la pelota, cuando realmente no debería hacerlo.
    
    def golpear(self, pelota):
        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho
            
Detectar el golpe de la pelota
Añadimos en el bucle principal del programa la llamada al método golpear() de la raqueta del jugador humano.

        raqueta_1.golpear(pelota)

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
 
Paso 9: Mostrar puntuación
En este útlimo paso, añadiremos la puntuación de la partida.

Para ello, crearemos unos contadores que se actualizarán al ganar uno de los dos jugadores y que se mostrarán en la ventana.

    # pong_1_9.py: Mostrar puntuación de la partida

    import random
    import pygame
    from pygame.locals import QUIT

    # Constantes para la inicialización de la superficie de dibujo
    VENTANA_HORI = 800  # Ancho de la ventana
    VENTANA_VERT = 600  # Alto de la ventana
    FPS = 60  # Fotogramas por segundo
    BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)
    NEGRO = (0, 0, 0)  # Color del texto (RGB)


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

        # Puntuación de la pelota
        self.puntuacion = 0
        self.puntuacion_ia = 0

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ia += 1
        if self.x >= VENTANA_HORI:
            self.reiniciar()
            self.puntuacion += 1
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
    pygame.display.set_caption("Pong 9")

    # Inicialización de la fuente
    fuente = pygame.font.Font(None, 60)

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

        texto = f"{pelota.puntuacion} : {pelota.puntuacion_ia}"
        letrero = fuente.render(texto, False, NEGRO)
        ventana.blit(letrero, (VENTANA_HORI / 2 - fuente.size(texto)[0] / 2, 50))

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


Las instrucciones añadidas con respecto al paso 8 son las siguientes:

Puntuación de los jugadores
Para guardar y actualizar la puntuación de los jugadores, añadimos las siguientes instrucciones:

Atributos puntuacion
Añadimos dos atributos más en la clase PelotaPong, puntuacion y puntuacion_ia para guardar las puntuaciones de cada jugador.

        # Puntuación de la pelota
        self.puntuacion = 0
        self.puntuacion_ia = 0

Modificar la puntuación
La puntuación debe modificarse cuando un jugador gana, es decir, cuando la pelota supera uno de los laterales. El programa detecta esa situación en el método rebotar de PelotaPong, así que añadimos en ese método las líneas 44 y 47.

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ia += 1
        if self.x >= VENTANA_HORI:
            self.reiniciar()
            self.puntuacion += 1

Para mostrar en la ventana la puntuación de ambos jugadores, añadimos las siguientes instrucciones:
Color del texto
Definimos el color NEGRO como constante:

    NEGRO = (0, 0, 0)  # Color del texto (RGB)
    
Definición del tamaño de fuente
Creamos un objeto de clase Font en el que definimos el tamaño del tipo de letra (con el primer argumento podríamos elegir un tipo de letra determinado, en este caso no indicamos ninguno y por tanto pygame usará el predeterminado)

    # Inicialización de la fuente
    fuente = pygame.font.Font(None, 60)

Escritura en la pantalla
Para escribir la puntuación:

línea 148: Creamos una variable con el texto a mostrar
línea 149: Creamos la superficie de dibujo con el texto e indicamos el color del texto.
línea 150: Dibujamos la superficie, indicando la posición (x, y). Como la posición es siempre la esquina superior izquierda, tenemos que desplazar la posición horizontal hacia la izquierda teniendo en cuenta el tamaño.
        
        texto = f"{pelota.puntuacion} : {pelota.puntuacion_ia}"
        letrero = fuente.render(texto, False, NEGRO)
        ventana.blit(letrero, (VENTANA_HORI / 2 - fuente.size(texto)[0] / 2, 50))
       
Por lo tanto el código de nuesto juego PingPong final quedaría de la siguiente manera:
mport random
    import pygame
    from pygame.locals import QUIT

    # Constantes para la inicialización de la superficie de dibujo
    VENTANA_HORI = 800  # Ancho de la ventana
    VENTANA_VERT = 600  # Alto de la ventana
    FPS = 60  # Fotogramas por segundo
    BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)
    NEGRO = (0, 0, 0)  # Color del texto (RGB)


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

        # Puntuación de la pelota
        self.puntuacion = 0
        self.puntuacion_ia = 0

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ia += 1
        if self.x >= VENTANA_HORI:
            self.reiniciar()
            self.puntuacion += 1
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
    pygame.display.set_caption("Pong 9")

    # Inicialización de la fuente
    fuente = pygame.font.Font(None, 60)

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

        texto = f"{pelota.puntuacion} : {pelota.puntuacion_ia}"
        letrero = fuente.render(texto, False, NEGRO)
        ventana.blit(letrero, (VENTANA_HORI / 2 - fuente.size(texto)[0] / 2, 50))

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
