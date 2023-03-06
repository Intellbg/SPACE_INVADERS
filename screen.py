import random
import sys
import pygame
from pygame.sprite import Group, spritecollideany
from sprites.block import Block
from sprites.button import Text
from sprites.lasser import Lasser
from sprites.missile import Missile
from sprites.obstacle import Obstacle
from sprites.ships.invader import Octopus, Squid, Invader
from sprites.ships.ufo import Ufo
from sprites.ships.defender import Defender
from pygame.image import load
from pygame.display import set_caption, set_mode, set_icon, update


class Screen():
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 563
    screen = set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    playing = False

    def __init__(self):
        set_caption("SPACE INVADERS")
        set_icon(load(r'assets/img/UfoRed.png').convert_alpha())
        self.font = pygame.font.Font(None, 70)
        self.font2 = pygame.font.SysFont("Consolas", 25)

    def displayTextScore(self):
        text = self.font2.render(f"Score: {self.score}", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (0, 0)
        self.screen.blit(text, textRect)

    def displayLife(self):
        text = self.font2.render(
            f"Life: {self.player.getLife()}", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.bottomleft = (0, self.SCREEN_HEIGHT)
        self.screen.blit(text, textRect)

    def displayGameover(self):
        gameover = True
        textGameover = self.font.render("GAME OVER", True, (255, 0, 128))
        textGameoverRect = textGameover.get_rect()
        textGameoverRect.center = (
            self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 - 75)

        text_surfaceScore = self.font.render(
            f"Score: {self.score}", True, (255, 177, 187))
        text_R = text_surfaceScore.get_rect()
        text_R.center = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 + 50)
        
        playText=Text(self.font2,"Jugar",self.SCREEN_WIDTH//2-40, self.SCREEN_HEIGHT//2+50)
        quitText=Text(self.font2,"Salir",self.SCREEN_WIDTH//2+40, self.SCREEN_HEIGHT//2+50)


        self.screen.fill(self.BLACK)
        while gameover:
            self.screen.blit(textGameover, textGameoverRect)
            self.screen.blit(text_surfaceScore, text_R)
            update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                gameover = False
        return gameover

    def createAliens(self,height):
        aliens = Group()
        for i in range(12):
            for j in range(5):
                if j == 0:
                    aliens.add(Squid(i, j+height, self.screen))
                elif j > 2:
                    aliens.add(Octopus(i, j+height, self.screen))
                else:
                    aliens.add(Invader(i, j+height, self.screen))
        return aliens

    def instanceSprites(self):
        self.player = Defender(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        obstacle = Obstacle(self.screen)
        missile = Missile.getInstance()
        lasser = Lasser.getInstance()
        ufo = Ufo.getInstance()

        aliens=self.createAliens(0)

        allSprites = Group()
        allSprites.add(aliens)
        allSprites.add(self.player)
        allSprites.add(missile)
        allSprites.add(lasser)
        allSprites.add(ufo)
        allSprites.add(obstacle.blocks)

        missileCollisionable = Group()
        missileCollisionable.add(aliens)
        missileCollisionable.add(obstacle.blocks)
        missileCollisionable.add(ufo)

        lasserCollisionable = Group()
        lasserCollisionable.add(self.player)
        lasserCollisionable.add(obstacle.blocks)

        return missile, lasser, aliens, ufo, missileCollisionable, lasserCollisionable, allSprites

    def playSpaceInvaders(self):
        self.playing = True
        clock = pygame.time.Clock()
        missile, lasser, aliens, ufo, missileCollisionable, lasserCollisionable, allSprites = self.instanceSprites()

        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.moveX(-1)
            if keys[pygame.K_RIGHT]:
                self.player.moveX(1)
            if keys[pygame.K_SPACE]:
                self.player.shoot()
            if keys[pygame.K_p]:
                self.pausar()

            if not ufo.hasAppeared():
                if random.randint(0, 1000) == 50:
                    ufo.setPosition(self.screen.get_width())

            randomEnemy = random.choice(aliens.sprites())
            randomEnemy.shoot()

            self.screen.fill(self.BLACK)
            allSprites.update()

            # Handle aliens of screen
            for alien in aliens:
                if alien.getY() > 400:
                    self.playing = False
                if not self.screen.get_rect().contains(alien):
                    aliens.update(screenCollision=True)
                    break

            missileCollision = spritecollideany(missile, missileCollisionable)
            if missileCollision:
                if isinstance(missileCollision, Block):
                    missileCollision.gotShoot()
                if isinstance(missileCollision, Invader):
                    self.score += missileCollision.getScore()
                    missileCollision.kill()
                    if len(aliens) == 0:
                        aliens=self.createAliens(140)
                if isinstance(missileCollision, Ufo):
                    self.score += missileCollision.getScore()
                    missileCollision.gotShoot()
                missile.removeFromScreen()

            lasserCollision = spritecollideany(lasser, lasserCollisionable)
            if lasserCollision:
                if isinstance(lasserCollision, Block):
                    lasserCollision.gotShoot()
                if isinstance(lasserCollision, Defender):
                    self.playing = lasserCollision.gotShoot()
                lasser.removeFromScreen()

            for entity in allSprites:
                self.screen.blit(entity.image, entity.rect)

            self.displayTextScore()
            self.displayLife()
            update()
            clock.tick(60)

    def pausar(self):
        pausa = True
        text_surfacePausa = self.font2.render("PAUSA", True, (255, 0, 128))
        text_pausa = text_surfacePausa.get_rect()
        text_pausa.center = (self.SCREEN_WIDTH // 2,
                             self.SCREEN_HEIGHT // 2 - 50)
        text_surfaceR = self.font2.render(
            "Presiona la tecla R para continuar", True, (255, 177, 187))
        text_R = text_surfaceR.get_rect()
        text_R.center = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 + 50)

        while pausa:
            self.screen.blit(text_surfacePausa, text_pausa)
            self.screen.blit(text_surfaceR, text_R)
            update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                pausa = False

    def displayStartScreen(self):
        displaying = True
        self.screen.fill(self.BLACK)
        self.font = pygame.font.SysFont("Consolas", 75)
        self.font2 = pygame.font.SysFont("Consolas", 40)
        title=Text(self.font,"SPACE INVADERS",self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2-50)
        playText=Text(self.font2,"Jugar",self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2+50)
        quitText=Text(self.font2,"Salir",self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2+100)
        
        while displaying:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    playText.checkHover(pos)
                    quitText.checkHover(pos)
                if event.type == pygame.MOUSEBUTTONUP:
                    if playText.getRect().collidepoint(pos):
                        displaying = False
                    if quitText.getRect().collidepoint(pos):
                        pygame.quit()
                        sys.exit()

            for button in [playText,quitText,title]:
                button.display(self.screen)
            update()
