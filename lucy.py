import pygame

#personaje
class Soul:
    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.image = pygame.image.load("img/cora.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.mover_derecha = False
        self.mover_izquierda = False
        self.mover_arriba = False
        self.mover_abajo = False
        
     #movimiento
    def mover(self):
         if self.mover_derecha:
             self.rect.x += 1
         if mover_izquierda:
             self.rect.x -= 1
         if mover_arriba:
             self.rect.y += 1
         if mover_abajo:
             self.rect.y -= 1
         
         
    #funcion para correr
    def corre(self):
        self.screen.blit(self.image, self.rect)