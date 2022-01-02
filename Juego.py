#importando librerias 
import pygame
import sys
from lucy import Soul

#clase del personaje
class Save:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Save your soul")
        self.color = (230, 230, 230)
        self.soul = Soul(self)
     #correr el juego   
    def corre_juego(self):
             while True:
                 for event in pygame.event.get():
                     #evento de salie
                     if event.type == pygame.QUIT:
                         sys.exit()
                     elif event.type == pygame.KEYDOWN:
                         #evento de movimiento
                         #derecha presionado
                         if event.key == pygame.K_RIGHT:
                             self.lucy.mover_derecha = True
                         #izquierda presionado
                         if event.key == pygame.K_LEFT:
                             self.lucy.mover_izquierda = True
                         #arriba presionado
                         if event.key == pygame.K_UP:
                             self.lucy.mover_arriba = True
                         #abajo presionado
                         if event.key == pygame.K_DOWN:
                             self.lucy.mover_arriba = True
                         #dejar de presionar
                     elif event.type == pygame.KEYUP:
                         #derecha sin presionar
                         if event.key == pygame.K_RIGHT:
                             self.lucy.mover_derecha = False
                         #izquierda sin presionar
                         if event.key == pygame.K_LEFT:
                             self.lucy.mover_izquierda = False
                        #arriba sin presionar
                         if event.key == pygame.K_UP:
                             self.lucy.mover_arriba = False
                        #abajo sin presionar
                         if event.key == pygame.K_DOWN:
                             self.lucy.mover_arriba = False
             #pantalla
             self.nave.mover()
             self.screen.fill(self.color)
             self.lucy.corre
             pygame.display.flip()
             
#llamando clases
if __name__ == "__main__":
    a = Save()
    a.corre_juego()
    
