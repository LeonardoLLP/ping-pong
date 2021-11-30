# Ping Pong

Autores:  
[Ana López Paloma](https://github.com/Analopez90)  
[Paula Naranjo Borrallo](https://github.com/paulaanb)  
[Leonardo Luque Paganelli](https://github.com/LeonardoLLP)

Historia de Pong
Aunque desde la aparición de los ordenadores programables en los años 40 del siglo XX se han escrito programas que podían considerarse juegos, se suele considerar que el primer videojuego fue Computer Tennis. Este videojuego fue creado en 1958 para la exposición anual del Laboratorio Nacional de Brookhaven (EEUU) y simulaba un pista de tenis vista lateralmente. El juego se visualizaba en la pantalla de un osciloscopio y se convirtió en la mayor atracción de esa exposición. Aunque al año siguiente la exposición contó con una versión mejorada, tras ella el equipo se desmontó para reutilizar los componentes en el Laboratorio.

Bastante años después, en septiembre de 1972, se comercializó la primera videoconsola de la historia dirigida a los hogares, Magnavox Odyssey. Esta videoconsola se conectaba a una pantalla de televisor y uno de los juegos incluidos era Table Tennis. En este juego cada jugador controlaba una paleta que golpeaba una pelota. El mismo año, pero en noviembre, la compañía Atari comercializó Pong, una de las primeras máquinas de arcade, destinadas a lugares públicos.

Pong, el videojuego

Con Pong, un juego trivial para los estándares actuales, empezaba la era moderna de los videojuegos. Pong es un juego de deportes en dos dimensiones que simula un tenis de mesa. El jugador controla en el juego una paleta moviéndola verticalmente en la parte izquierda de la pantalla, y puede competir tanto contra un oponente controlado por computadora, como con otro jugador humano que controla una segunda paleta en la parte opuesta. Los jugadores pueden usar las raquetas para pegarle a la pelota hacia un lado u otro. El objetivo consiste en que uno de los jugadores consiga más puntos que el oponente al finalizar el juego. Estos puntos se obtienen cuando el jugador adversario falla al devolver la pelota.

La palabra Pong es una marca registrada por Atari Interactive (aunque la patente del juego la tuvo la empresa de Magnavox Odyssey), pero la palabra genérica "pong" se usa para describir el género de videojuegos.

Por todo ello, cuando se aprende a programar videojuegos, es habitual comenzar programando un juego como Pong, por su sencillez y también como homenaje al gran clásico.

Pygame
Pygame es un conjunto de módulos de Python que facilitan la creación de videojuegos. Pygame utiliza internamente la biblioteca SDL (Simple DirectMedia Layer), escrita principalmente en C.

Pygame se distribuye bajo la licencia libre LGPL, lo que permite utilizarla tanto en proyecto libres como comerciales.

Además de la Documentación oficial de pygame, en Internet se pueden encontrar sitios y libros dedicados a la introducción a la programación en general, o a la introducción a la programación de videojuegos en particular, mediante pygame, como los siguientes:

Programar Juegos Arcade con Python y Pygame
Making Games with Python & Pygame
Instalación de pygame
Los pasos para instalar pygame como módulo de sistema en Windows son los siguientes:

Abra una ventana de terminal y escriba los siguientes comandos.
Actualice pip:
python -m pip install --upgrade pip
Instale pygame:
pip install pygame
Realización del programa
Vamos a programar un juego de Pong en el que una de las raquetas esté controlada por el jugador humano mediante el teclado y la otra raqueta esté contralada por el propio programa.

Para la realización del juego Pong, iremos por fases, implementando en cada paso uno de los elementos del programa.
