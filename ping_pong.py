from pygame import *
from random import randint

font.init()
font1 = font.Font(None, 80)
lose = font1.render('GAME OVER!!', True, (0, 0, 0))

p_speed = 8
game_over = False
class GameSprite(sprite.Sprite):
   #class constructor
   def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
       super().__init__()
       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       #every sprite must have the rect property – the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 8:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 445:
           self.rect.y += self.speed
    def right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 8:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 445:
           self.rect.y += self.speed
speed_x = 2
speed_y = 2
class Ball(GameSprite):
    def update(self):
        global game_over
        global speed_x
        global speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.x > 475 or self.rect.x < 5:
            game_over = True
        if sprite.collide_rect(player_l, ball):
            speed_x *= -1            
            
        if sprite.collide_rect(player_r, ball):
            speed_x *= -1
        
        if self.rect.y < 5 or self.rect.y > 500:
            speed_y *= -1
            



back=(194, 251, 251)
win_width = 500
win_height = 550
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
player_r = Player('pong_1.png',5,225,20,100,p_speed)
player_l = Player('pong_1.png',475,225,20,100,p_speed)
ball = Ball('Ball.png', 250, 275, 50, 50, 1)

game = True
finish = False
clock = time.Clock()
FPS = 60

txt_location = (250,150)


while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
           game = False
  
    if finish != True:
        player_r.reset()
        player_r.left()
        player_l.reset()
        player_l.right()
        ball.reset()
        ball.update()

    if game_over == True :
        window.blit(lose,(60, 275))
        time.delay(500)
        finish = True

        

    


    
    display.update()
    clock.tick(FPS)
