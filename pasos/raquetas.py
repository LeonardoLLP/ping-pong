import paso5
import variables

#Creamos las raquetas
raqueta_1 = paso5.RaquetaPong()
raqueta_1.x = 60

raqueta_2 = paso5.RaquetaPong()
raqueta_2.x = variables.VENTANA_HORI - 60 - raqueta_2.ancho

#Dibujar las raquetas
variables.ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
variables.ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))