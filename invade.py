import pygame
import random

pygame.init()  # Initialize pygame

screen = pygame.display.set_mode((800, 600))  # Set up the display

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('shipp.png')
playerX = 370
playerY = 480

# Enemy
enemyimg = pygame.image.load('ufo.png')
enemyX = random.randint(0, 736)  # Random start position
enemyY = 50
enemy_speed = 0.3  # Speed of downward movement

move_left = move_right = False

def player(x, y):
    screen.blit(playerimg, (x, y))  # Draw the player

def enemy(x, y):
    screen.blit(enemyimg, (x, y))  # Draw the enemy

# Game loop
running = True
while running:
    screen.fill((0, 0, 100))  # Background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True

        # Key release events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False

    # Player movement
    if move_left:
        playerX -= 0.5
    if move_right:
        playerX += 0.5

    # Boundary check for player
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyY += enemy_speed
    if enemyY >= 600:  # If enemy reaches the bottom, reset it
        enemyY = 50
        enemyX = random.randint(0, 736)

    player(playerX, playerY)  # Draw the player
    enemy(enemyX, enemyY)  # Draw the enemy

    pygame.display.update()  # Refresh display
