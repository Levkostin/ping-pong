from pygame import*
game = True
#pygame.init()
window = display.set_mode((1000,600))
clock = time.Clock()
fon = transform.scale( image.load('bb.jpg'),(1000,600))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def go(self):
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_w:
                    self.rect.y += -1 * self.speed
#class

raketka_1 = GameSprite('Без названия (1).png', 50,300,40,200,10)

#raketka_2 = GameSprite('Без названия.png'300,950,100,40,200,10)









while game:
    window.blit(fon,(0,0))
    clock.tick(60)
    raketka_1.reset()
    raketka_1.go()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
