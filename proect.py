from pygame import*
from random import randint

class Game_sprite():
    def __init__(self, img, w, h, x, y):
        self.image = transform.scale(img, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        screen.blit(self.image, self.rect)

class Chopa(Game_sprite):
    def __init__(self):
        super().__init__(image.load('chopa.png'),95 , 110, 130, 455)
        self.costumes =[image.load('chopa.png'), image.load('chopa2.png'), image.load('chopa3.png'), image.load('chopa4.png'), image.load('chopa5.png'), image.load('chopa6.png')]
        for i in range(len(self.costumes)):
            self.costumes[i] = transform.scale(self.costumes[i], (95, 110))
        self.costume = 0
        self.isJump = False
        self.jumpCount = -21

    def update(self):
        self.costume += 1
        if self.costume > 29:
            self.costume = 0
        self.image = self.costumes[self.costume//5]
        if self.isJump:
            self.rect.y += self.jumpCount
            self.jumpCount += 1
            if self.jumpCount > 21:
                self.jumpCount = -21
                self.isJump = False

        super().update()

class Suriken(Game_sprite):
    def __init__(self): 
        super().__init__(image.load('suriken.png'),90 , 90, 900, 450)
        self.costumenum = 0
        self.costum =[image.load('suriken.png'), image.load('suriken2.png'), image.load('suriken3.png'), image.load('suriken4.png'), image.load('suriken5.png'), image.load('suriken6.png')]
        for i in range(len(self.costum)):
            self.costum[i] = transform.scale(self.costum[i], (90, 90))

    def update(self):
        global score, scoretext
        if self.rect.x <= -70:
            self.rect.x = 960
            score += 10
            scoretext = f.render(str(score), 1, (0, 0, 0))
        self.rect.x -= 10
        self.costumenum += 1
        if self.costumenum >= len(self.costum)*5 -1:
            self.costumenum = 0
        self.image = self.costum[self.costumenum // 5]
        super().update()

screen = display.set_mode((900, 600))
display.set_caption('Japan Chopa')
background = transform.scale(image.load('fonk1.png'), (900,600))
chopa = Chopa()
suriken = Suriken()

button_play = transform.scale(image.load('play.png'), (250, 250))
button_quit = transform.scale(image.load('exit.png'), (250, 250))

clock = time.Clock()
game = True
menu = True
finish = True


score = 0
font.init()
f = font.Font(None, 65)
scoretext = f.render(str(score), 1, (0, 0, 0))

highscore = 0
with open('highscore.txt', 'r') as file:
    highscore = int(file.read())

hightext = f.render('Points: ' + str(highscore), 1, (0, 0, 0))

while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                chopa.isJump = True
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                x, y = mouse.get_pos()
                if menu:
                    if x > 350 and x < 600 and y > 100 and y < 350:
                        menu = False
                        finish = False
                    if x > 350 and x < 600 and y > 300 and y < 550:
                        game = False

    screen.blit(background, (0,0))
    if menu:
        screen.blit(button_play, (350, 100))    
        screen.blit(button_quit, (350, 300))
        score = 0 
    elif not (finish):
        if chopa.rect.colliderect(suriken.rect):
            finish = True
            menu = True
            chopa = Chopa()
            suriken = Suriken()

        chopa.update()
        suriken.update()
        screen.blit(scoretext, (450, 130))
    display.update()


with open('highscore.txt', 'w') as file:
    file.write(str(highscore))  