import pygame
from snake import Snake, Direction

pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False
 
blueColor = pygame.color.Color(0, 0, 255)
rect = pygame.Rect(0, 0, 32, 32)

snake = Snake(0,0)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    snake.move(Direction.Right.value)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    snake.move(Direction.Left.value)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    snake.move(Direction.Down.value)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    snake.move(Direction.Up.value)

                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((0, 0, 0))
        for node in snake.getBody():
            pygame.draw.rect(screen, blueColor, node)
        pygame.display.flip()

