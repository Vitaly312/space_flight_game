import pygame
from meteorite import Meteorite
from random import randint
pygame.init()
images = pygame.image.load('images/fon.jpg')
rect = images.get_rect()
font = pygame.font.SysFont("comicsansms", 25)


def update_screen(screen, my_settings, ship, meteorites):
    """
    Обновляет экран и координаты всех обьектов.
    В случае столкновения заканчивает игру
    """
    global images, rect, font
    image = pygame.transform.scale(images, screen.get_size())
    screen_rect = screen.get_rect()
    my_settings.screen_width, my_settings.screen_height = screen.get_size()
    screen.blit(image, rect)
    ship.rect.bottom = screen_rect.bottom
    ship.update()
    ship.blitme()
    make_meteorite(screen, my_settings, meteorites)
    del_meteorite(my_settings, meteorites)
    for meteorite in meteorites:
        meteorite.update()
    if pygame.sprite.spritecollideany(ship, meteorites):
        my_settings.aktive = False
    meteorites.draw(screen)
    value = font.render("Ваш счёт: " + str(my_settings.points), True, 'yellow')
    screen.blit(value, [0, 0])
    pygame.display.flip()


def check_event(ship, my_settings):
    """обработка всех событий, происходящих во время игры"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            my_settings.aktive = False
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, my_settings)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship, my_settings):
    """обработка нажатий клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_q:
        my_settings.aktive = False


def check_keyup_events(event, ship):
    """обработка поднятия клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def make_meteorite(screen, my_settings, meteorites):
    """создает новый метеорит, если количество метеоритов не максимальное"""
    if len(meteorites) < my_settings.max_meteorites:
        if randint(1, 3) == 3:  # Каждый 3 метеорит должен быть другого размера
            new_meteorite = Meteorite(screen, my_settings, 1)
        else:
            new_meteorite = Meteorite(screen, my_settings, 0)
        x = randint(1, my_settings.screen_width)
        y = randint(-500, -25)
        new_meteorite.rect.x = x
        new_meteorite.rect.y = y
        if not pygame.sprite.spritecollideany(new_meteorite, meteorites):
            meteorites.add(new_meteorite)


def del_meteorite(my_settings, meteorites):
    """ удаляет старые метеориты """
    for meteorite in meteorites:
        if meteorite.rect.y >= my_settings.screen_height:
            meteorites.remove(meteorite)
            my_settings.points += 1
