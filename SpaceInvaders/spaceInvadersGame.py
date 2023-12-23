import pygame as pg
import random

# initialize pygame
pg.init()
game_running = True

# global variables
width = 800
height = 600
player_x = width/2
player_y = height - 100
ship_speed_factor = 1
ship_speed = 0

enemy_x = random.randint(0, 735)
enemy_y = random.randint(50, 150)
enemy_speed_factor = 2
enemy_x_speed = enemy_speed_factor
enemy_y_drop = 30

bullet_x = 0
bullet_y = height - 100
bullet_speed_factor = 5
bullet_speed = bullet_speed_factor
current_bullet_x = -800
bullet_state = "ready"

score = 0

# create the screen
screen = pg.display.set_mode((width, height))

background = pg.image.load("images/background.png")

# title and icon (www.flaticon.com)
pg.display.set_caption("Space Invaders 2022")
icon = pg.image.load("images/ufo.png")
pg.display.set_icon(icon)

# render player's ship and enemy
player_image = pg.image.load("images/player.png")
enemy_image = pg.image.load("images/enemy.png")
bullet_image = pg.image.load("images/bullet.png")

def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y):
    screen.blit(enemy_image, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))

def hit_enemy(enemy_x, enemy_y, current_bullet_x, bullet):
    bullet_to_enemy_distance = ((enemy_x - current_bullet_x)**2 + (enemy_y - bullet_y)**2)**(0.5)
    if bullet_to_enemy_distance < 27:
        return True
    else:
        return False

while game_running:

    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_running = False
        if event.type == pg.KEYDOWN:
            if (event.key == pg.K_LEFT):
                ship_speed = -1 * ship_speed_factor
            if (event.key == pg.K_RIGHT):
                ship_speed = 1 * ship_speed_factor
            if (event.key == pg.K_SPACE) and bullet_state == "ready":
                fire_bullet(player_x, bullet_y)
                current_bullet_x = player_x
                bullet_state = "fire"
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                ship_speed = 0

    player_x += ship_speed
  
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    enemy_x += enemy_x_speed

    if enemy_x <= 0:
        enemy_x_speed = enemy_speed_factor
        enemy_y += enemy_y_drop
    elif enemy_x >= 736:
        enemy_x_speed = -1 * enemy_speed_factor
        enemy_y += enemy_y_drop
    
    if bullet_state == "fire":
        fire_bullet(current_bullet_x, bullet_y)
        bullet_y -= bullet_speed

    if bullet_y <= 0:
        bullet_state = "ready"
        bullet_y = height - 100

    collision = hit_enemy(enemy_x, enemy_y, current_bullet_x, bullet_y)
    
    if collision:
        bullet_y = height - 100
        bullet_state = "ready"
        score += 1
        print(score)
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(50, 150)
    
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    
    pg.display.update()