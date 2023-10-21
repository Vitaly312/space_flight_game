import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from tkinter import *
from tkinter.ttk import Radiobutton

clock = pygame.time.Clock()
my_settings = Settings()
max_point_1, max_point_2, max_point_3 = 0, 0, 0


def run_game():
    screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height), pygame.RESIZABLE)
    ship = Ship(screen, my_settings)
    meteorites = Group()
    gf.update_screen(screen, my_settings, ship, meteorites)
    pygame.time.wait(1000)
    my_settings.points = 0
    my_settings.aktive = True
    while my_settings.aktive:  # main game loop
        gf.check_event(ship, my_settings)
        gf.update_screen(screen, my_settings, ship, meteorites)
        clock.tick(60)
    del ship, meteorites
    pygame.time.wait(500)
    pygame.display.quit()
    return my_settings.points


def start():
    level = selected.get()
    if level == 1:  # изменяем настройки в зависимости от выбранного уровня
        my_settings.max_meteorites = 6
    if level == 2:
        my_settings.max_meteorites = 9
    if level == 3:
        my_settings.max_meteorites = 11
        my_settings.meteorite_speed = 12
        my_settings.ship_speed = 10
    point = run_game()
    txt = "Ваш счет: " + str(point)
    global max_point_1, max_point_2, max_point_3
    if max_point_1 < point and level == 1:
        max_point_1 = point
        txt += ' (Рекорд!)'
    elif max_point_2 < point and level == 2:
        max_point_2 = point
        txt += ' (Рекорд!)'
    elif max_point_3 < point and level == 3:
        max_point_3 = point
        txt += ' (Рекорд!)'
    lbl_point.configure(text=f"--  Record  --\nEasy -- {max_point_1}"
                             f"\nNormal -- {max_point_2}\nHard -- {max_point_3}")
    lbl.configure(text=txt, font=25)


window = Tk()
window.geometry('1200x800')
btm = Button(window, text="Play", fg="red", font=("Arial Bold", 50),
             command=start)
btm.place(relx=0.5, rely=0.5, anchor='center')
lbl = Label(window)
lbl.place(relx=0.5, rely=0.7, anchor='center')
lbl_point = Label(window, text='--  Record  --\nEasy -- 0 \nNormal -- 0\nHard -- 0', font=("Helvetica", 12))
lbl_point.place(relx=0.5, rely=0.85, anchor='center')
lbl2 = Label(window, text='-- Выберите сложность --', font=5)
lbl2.place(relx=0.5, rely=0.01, anchor='n')

selected = IntVar()
selected.set(2)
rad1 = Radiobutton(window, text='EASY', value=1, variable=selected)
rad2 = Radiobutton(window, text='NORMAL', value=2, variable=selected)
rad3 = Radiobutton(window, text='HARD', value=3, variable=selected)
rad1.place(relx=0.3, rely=0.08, anchor='n')
rad2.place(relx=0.5, rely=0.08, anchor='n')
rad3.place(relx=0.7, rely=0.08, anchor='n')
window.mainloop()
