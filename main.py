import pygame as pg
from random import randint

pg.init()

#GREEN = (50, 255, 150)

WIN_SIZE = (800, 600)
x, y = 0, 1




class BaseSprite(pg.sprite.Sprite):
    def __init__(self, filename, x, y, w, h, speed_x=0, speed_y=0):
        super().__init__()
        self.rect = pg.Rect(x, y, w, h)
        self.image = pg.transform.scale(pg.image.load(filename), (w, h))
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y




class Hero(BaseSprite):   
    energy=0
    max_energy = 25
    points = 0


    def update(self):
        self.energy+=1
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed_y
            if self.rect.y > WIN_SIZE[y] - self.rect.height:
                self.rect.y = WIN_SIZE[y] - self.rect.height
        if keys[pg.K_UP]:
            self.rect.y -= self.speed_y
            if self.rect.y < 0:
                self.rect.y = 0
        if keys[pg.K_SPACE]:
            self.fire()



    class UFO (BaseSprite):
     def update(self):
        global ufo_miseb
        super().update() 
        if self.rect.y > WIN_SIZE[y]:
            ufos.remove(self)
            ufo_miseb+=1



def set_text(test, x, y, color=(255,255,200,)):
    mw.blit(
        font1.render(test, True, color),(x,y)
    )

font1 = pg.font.Font(None, 36)

ball = BaseSprite ('ball2.png', 160, 200, 50, 50 ,speed_x=0, speed_y=0,   )


  
  # двигаем мяч
ball.rect.x += speed_x
ball.rect.y += speed_y

  # если мяч достиг края экрана меняем скорость на противоположную
if  ball.rect.y < 0:
    speed_y *= -1
if ball.rect.x > 450 or ball.rect.x < 0:
    speed_x *= -1

  # если мяч столкнулся с платформой меняем скорость на противоположную
if ball.rect.colliderect(platform.rect):
    speed_y *= -1


def make_UFO():
    speed = randint(3, 5)
     
    ufo= UFO('ufo.png', randint(0, WIN_SIZE[x]-80), -100, 80, 60, 0, speed)
    ufos.append(ufo)






mw = pg.display.set_mode(WIN_SIZE)

clock = pg.time.Clock()


fon = pg.transform.scale(fon, WIN_SIZE)

hero = Hero('koshka.png', WIN_SIZE[x]/2, WIN_SIZE[y]-100, 80, 80, 5, 5)





ufo_miseb = 0



play = True 
game = True

ticks = 0


while game:
   

    for event in  pg.event.get():
        if event.type == pg.QUIT:
            game = False
    
    if play:
        
        if ticks %60 == 0:
            make_UFO()

        mw.blit(fon, (0, 0))

        hero.update()
        hero.draw()
        
      

        for ufo in ufos:
                ufo.update()
                ufo.draw()

   
    
    
    
        collisides = pg.sprite.groupcollide(dranik, ufos, True, True)
        for dranik,ufo in collisides.items():
            hero.points += 1
        
        set_text(f"пропушено {ufo_miseb}", 45, 50)
        set_text(f"очк {ufo_miseb}", 45, 50)

    pg.display.update()
    clock.tick(60)
    ticks += 1