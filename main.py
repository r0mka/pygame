import pygame as pg

# initialize pygame
pg.init()
run = True

WIN_DIM = WIN_WIDTH, WIN_HEIGHT = 800, 600
HERO_DIM = HERO_WIDTH, HERO_HEIGHT = 50, 100

win = pg.display.set_mode(WIN_DIM)
pg.display.set_caption("First Game")



hero_pos = [0, 0]
hero_vel = [5, 5]


def redraw_window():
    win.fill((0, 0, 0))
    pg.draw.rect(win, (255, 0, 0), (hero_pos[0], hero_pos[1], HERO_WIDTH, HERO_HEIGHT))
    pg.display.update()


   
clock = pg.time.Clock()

while run: 
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = false

    keys = pg.key.get_pressed()
    
    
    if keys[pg.K_LEFT] and hero_pos[0] >= hero_vel[0]:
        hero_pos[0] -= hero_vel[0]
    if keys[pg.K_RIGHT] and hero_pos[0] + hero_vel[0] <= WIN_WIDTH - HERO_WIDTH:
        hero_pos[0] += hero_vel[0]
    if keys[pg.K_UP] and hero_pos[1] >= hero_vel[1]:
        hero_pos[1] -= hero_vel[1]
    if keys[pg.K_DOWN]:
        hero_pos[1] += hero_vel[1]


    redraw_window()

    
pg.quit()    



