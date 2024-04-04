from pygame import*
game = True
#pygame.init()
window = display.set_mode((1000,600))
fon  = image.load('bb.jpg')
transform.skale('bb.jpg',1000,600)








while game:
    window.blit(fon,(0,0))
    display.update()
clock.tick(60)