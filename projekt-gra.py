import pygame
import random

pygame.init()
clock = pygame.time.Clock()
fps = 60

# logo gry
logo = pygame.image.load("cuteghost1.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("materializedGhost")

font = pygame.font.SysFont('Arial Black', 50)

szerokosc = 500
wysokosc = 500
# ekran
window = pygame.display.set_mode((szerokosc, wysokosc))

# grafika
tlo = pygame.image.load("@jonahvinet.png")
ziemia = pygame.image.load("bgziemia.png")
koniec = pygame.image.load("gameover.png")

koniec_rect = koniec.get_rect(center=(250, 200))


def punktacja():
    wynik = font.render(str(score), True, (255, 255, 255))
    wynik_rect = wynik.get_rect(center=(szerokosc / 2, 40))
    window.blit(wynik, wynik_rect)
    return


# zmienne
score = 0

przewijanie_ziemi = 0
szybkosc = 2

# duch
duch = pygame.image.load("cuteghost1.png").convert_alpha()
duch_rect = duch.get_rect()
duch_rect.x = 100
duch_rect.y = 200

# przeszkody
szybkosc_lotu = 5
szybkosc_lotu2 = 6
szybkosc_lotu3 = 7
szybkosc_lotu4 = 5
szybkosc_lotu5 = 4

przeszkoda = pygame.image.load("nietoperzyk.png").convert_alpha()
przeszkoda2 = pygame.image.load("nietoperzyk.png").convert_alpha()
przeszkoda3 = pygame.image.load("czacha.png").convert_alpha()
przeszkoda4 = pygame.image.load("czacha.png").convert_alpha()
przeszkoda5 = pygame.image.load("cutedynia.png").convert_alpha()

rect = przeszkoda.get_rect()
rect2 = przeszkoda2.get_rect()
rect3 = przeszkoda3.get_rect()
rect4 = przeszkoda4.get_rect()
rect5 = przeszkoda5.get_rect()
rect.center = (500, 50)
rect2.center = (550, 320)
rect3.center = (520, 150)
rect4.center = (550, 100)
rect5.center = (560, 290)

space = False
move_up = False
move_down = False
start = True
running = True
while running:

    clock.tick(fps)
    # ustawienie tła
    pygame.display.flip()
    window.blit(tlo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_SPACE:
                space = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_SPACE:
                space = False

    if duch_rect.colliderect(rect) or duch_rect.colliderect(rect2) or \
            duch_rect.colliderect(rect3) or duch_rect.colliderect(rect4) or \
            duch_rect.colliderect(rect5):
        start = False

    if start:
        # poruszanie duchem
        if move_up:
            duch_rect.y -= 5
        if move_down:
            duch_rect.y += 5

        # ograniczenia postaci nie mozna wyjsc poza obszar
        if duch_rect.y <= 0:
            duch_rect.y = 0
        if duch_rect.y >= 380:
            duch_rect.y = 380

        # wynik
        score = score + 1
        punktacja()

        # poruszanie przeszkód
        rect.x -= szybkosc_lotu
        if rect.x < -130:
            # wraca do porządku szerokości ekanu
            rect.x = szerokosc
            rect.y = random.randint(0, 380)
            rect.x -= szybkosc_lotu

        rect2.x -= szybkosc_lotu2
        if rect2.x < -130:
            rect2.x = szerokosc + 50
            rect2.y = random.randint(0, 380)
            rect2.x -= 6

        rect3.x -= szybkosc_lotu3
        if rect3.x < -31:
            rect3.x = szerokosc + 25
            rect3.y = random.randint(0, 380)
            rect3.x -= szybkosc_lotu3

        rect4.x -= szybkosc_lotu4
        if rect3.x < -31:
            rect4.x = szerokosc + 25
            rect4.y = random.randint(0, 380)
            rect4.x -= szybkosc_lotu4

        rect5.x -= szybkosc_lotu5
        if rect5.x < -65:
            rect5.x = szerokosc + 40
            rect5.y = random.randint(0, 380)
            rect5.x -= szybkosc_lotu5

        window.blit(duch, (duch_rect.x, duch_rect.y))
        window.blit(przeszkoda, rect)
        window.blit(przeszkoda2, rect2)
        window.blit(przeszkoda3, rect3)
        window.blit(przeszkoda4, rect4)
        window.blit(przeszkoda5, rect5)

        # ustawienie podłoża
        window.blit(ziemia, (przewijanie_ziemi, 400))
        # szybkość przewijania w lewo
        przewijanie_ziemi -= szybkosc
        if abs(przewijanie_ziemi) >= 400:
            przewijanie_ziemi = 0

    else:
        window.blit(koniec, koniec_rect)
        rect.x = 0
        rect2.x = 0
        rect3.x = 0
        rect4.x = 0
        rect5.x = 0

        punktacja()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if event.key == pygame.K_SPACE:
                        space = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        space = False

        if space:
            space = False
            start = True

            score = 0
            rect.center = (550, 200)
            rect2.center = (600, 300)
            rect3.center = (605, 150)
            duch_rect.x = 100
            duch_rect.y = 200

    pygame.display.update()
pygame.quit()
