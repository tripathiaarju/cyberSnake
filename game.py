import pygame
import random
import os

# Initialize pygame
pygame.init()

# Screen dimensions and grid size
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (10, 10, 10)
CYBER_GREEN = (0, 255, 120)
DARK_GREEN = (0, 100, 60)
RED = (255, 60, 60)
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Snake Game")

# Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 10

# Font for displaying score
font = pygame.font.SysFont("consolas", 24)


def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, CYBER_GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(segment[0]+2, segment[1]+2, GRID_SIZE-4, GRID_SIZE-4))


def draw_food(position):
    pygame.draw.ellipse(screen, RED, pygame.Rect(position[0], position[1], GRID_SIZE, GRID_SIZE))


def draw_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def random_food_position(snake):
    while True:
        x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
        y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        if (x, y) not in snake:
            return (x, y)


def game_loop():
    snake = [(GRID_SIZE * 5, GRID_SIZE * 5)]
    direction = (GRID_SIZE, 0)
    food = random_food_position(snake)
    score = 0

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)
        draw_grid()
        draw_snake(snake)
        draw_food(food)
        draw_score(score)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, GRID_SIZE):
            direction = (0, -GRID_SIZE)
        if keys[pygame.K_DOWN] and direction != (0, -GRID_SIZE):
            direction = (0, GRID_SIZE)
        if keys[pygame.K_LEFT] and direction != (GRID_SIZE, 0):
            direction = (-GRID_SIZE, 0)
        if keys[pygame.K_RIGHT] and direction != (-GRID_SIZE, 0):
            direction = (GRID_SIZE, 0)

        # Update snake position
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Check for collisions
        if (new_head in snake or
                new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT):
            running = False
            break

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = random_food_position(snake)
        else:
            snake.pop()

    pygame.quit()


# Run the game
game_loop()
