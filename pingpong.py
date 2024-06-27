from pygame import *

#PREMENNE
FPS = 40
WIN_WIDTH = 800
WIN_HEIGHT = 600
run = True
clock = time.Clock()

#OBRAZ
window = display.set_mode((WIN_WIDTH,WIN_HEIGHT))
display.set_caption("Pingpong")


#TRIEDA
class Player(sprite.Sprite):
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
        self.rect = draw.rect(window,color,(x,y,width,height))
#DRAW       
    def draw(self):
        draw.rect(window,self.color,(self.rect.x, self.rect.y, self.width, self.height))
#UPDATY
    def update_right(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 0 :
            self.rect.y = self.rect.y - self.speed
        if keys[K_s] and self.rect.y < WIN_HEIGHT - self.height:
            self.rect.y = self.rect.y + self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 0 :
            self.rect.y = self.rect.y - self.speed
        if keys[K_DOWN] and self.rect.y < WIN_HEIGHT - self.height:
            self.rect.y = self.rect.y + self.speed


#TRIEDA
class Ball(sprite.Sprite):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_y = 5
        self.speed_x = 5
        self.rect = draw.circle(window,color,(x,y),radius)
#DRAW
    def draw(self):
        draw.circle(window,(255,255,255),(self.rect.x, self.rect.y),self.radius)
#UPDATE
    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y

        if self.rect.y < 0 or self.rect.y > WIN_HEIGHT :
            self.speed_y *= -1

#OBJEKTY        
player1 = Player(5,100,20,100,(255,0,0))
player2 = Player(WIN_WIDTH - 25,100,20,100,(0,255,0))
ball = Ball(100,100,20,(255,255,255))
#TEXT
font.init()
font = font.Font(None,35)
lose1 = font.render("player1 lost",True,(180,0,0))
lose2 = font.render("player2 lost",True,(180,0,0))

#SLUCKA
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill((0,0,0))
    player1.draw()
    player2.draw()
    ball.draw()
    player1.update_right()
    player2.update_left()
    ball.update()

    if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
        ball.speed_x *= -1

    if ball.rect.x > WIN_WIDTH :
        window.blit(lose2,(200,200))

    if ball.rect.x < 0:
        window.blit(lose1,(200,200))

    display.update()
    clock.tick(FPS)
quit()