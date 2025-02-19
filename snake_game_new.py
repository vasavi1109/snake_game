import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
window_x = 720
window_y = 480

# Snake settings
snake_block = 10
snake_speed = 10  # Adjusted for better playability

# Initialize game window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Font settings
font_style = pygame.font.SysFont("times new roman", 20)
def show_score(score, x=10, y=10):
    value = font_style.render(f"Score: {score}", True, white)
    game_window.blit(value, [x, y])

def game_over(score):
    game_window.fill(black)
    message = font_style.render(f"Game Over! Your Score: {score}", True, red)
    game_window.blit(message, [window_x / 3, window_y / 3])
    pygame.display.update()
    time.sleep(2)  # Display score for 2 seconds before exiting
    pygame.quit()
    quit()

def game_loop():
    x, y = window_x / 2, window_y / 2
    x_change, y_change = 0, 0
    snake_list = [[x, y]]
    length_of_snake = 1
    
    food_x = random.randrange(0, window_x - snake_block, 10)
    food_y = random.randrange(0, window_y - snake_block, 10)
    
    direction = 'RIGHT'
    change_to = direction
    
    score = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
        
        direction = change_to
        if direction == 'UP':
            y -= snake_block
        elif direction == 'DOWN':
            y += snake_block
        elif direction == 'LEFT':
            x -= snake_block
        elif direction == 'RIGHT':
            x += snake_block
        
        if x >= window_x or x < 0 or y >= window_y or y < 0:
            game_over(score)
        
        snake_head = [x, y]
        snake_list.insert(0, snake_head)
        if len(snake_list) > length_of_snake:
            snake_list.pop()
        
        for segment in snake_list[1:]:
            if segment == snake_head:
                game_over(score)
        
        if x == food_x and y == food_y:
            score += 10
            length_of_snake += 1
            food_x = random.randrange(0, window_x - snake_block, 10)
            food_y = random.randrange(0, window_y - snake_block, 10)
        
        game_window.fill(black)
        for pos in snake_list:
            pygame.draw.rect(game_window, green, [pos[0], pos[1], snake_block, snake_block])
        pygame.draw.rect(game_window, red, [food_x, food_y, snake_block, snake_block])
        
        show_score(score)
        pygame.display.update()
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

game_loop()
