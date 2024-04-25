from pygame import*
game = True
#pygame.init()
speed_x = 10
speed_y = 10 
window = display.set_mode((1000,600))
clock = time.Clock()
fon = transform.scale(image.load('bb.jpg'),(1000,600))

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
        keys = key.get_pressed() #check the key pressed
        if keys[K_w]:
            self.rect.y += -1 * self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        if self.rect.y == 400:
            self.rect.y -= self.speed
        if self.rect.y == 0:
            self.rect.y += self.speed
    def gou(self):
        keys = key.get_pressed() #check the key pressed
        if keys[K_UP]:
            self.rect.y += -1 * self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        if self.rect.y == 400:
            self.rect.y -= self.speed
        if self.rect.y == 0:
            self.rect.y += self.speed
    def went(self):
        global speed_x 
        global speed_y
        if  self.rect.y <= 0:
            speed_y *= -1
        if self.rect.y >= 540:
           speed_y *= -1
        if self.rect.x >= 940:
            speed_x *= -1
        if self.rect.x <= 0:
            speed_x *= -1
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    

raketka_1 = GameSprite('Без названия (1) (1).png', 10,300,40,200,10)
raketka_2 = GameSprite('Без названия.png', 950,300,40,200,10)
ball = GameSprite('Без названия (16).jpg', 500,300,60,60,10)
player_1 = 0
player_2 = 0










while game:
    window.blit(fon,(0,0))

    raketka_1.reset()
    raketka_1.go()
    raketka_2.reset()
    raketka_2.gou()
    ball.reset()
    ball.went()
    font.init()
    font1 = font.SysFont('Arial',36)
    text_lose = font1.render(
        'USA: ' + str(player_2),1,(0,55,255)
    )
    text_win = font1.render(
        'SSSR: ' + str(player_1),1,(55,255,0)
    )
    window.blit(text_lose,(50,20))
    window.blit(text_win,(800,20))
        
    for e in event.get():
        if e.type == QUIT:
            game = False
            quit()  
    
    if ball.rect.x == 0:
        player_1 += 1
    if ball.rect.x == 940:
        player_2 += 1
    if sprite.collide_rect(raketka_1,ball):
        speed_x *= -1
    if sprite.collide_rect(raketka_2,ball):
        speed_x *= -1

    clock.tick(60)
    display.update()
