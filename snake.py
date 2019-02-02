import pygame
import time
import random
pause = False
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 100, 0)
clock = pygame.time.Clock()
display_width = 800
display_height = 600
pygame.init()
gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snaky')

font = pygame.font.SysFont(None, 25)


def screenText(msg, color):
    message = font.render(msg, True, color)
    gamedisplay.blit(message,[display_width/2,display_height/2])


def snake(block_size, snakelist):
    for XnY in snakelist:
        gamedisplay.fill(green, rect=[XnY[0], XnY[1], block_size, block_size])


def gameloop():
    GameExit = False
    GameOver = False
    x_pos = display_width / 2
    y_pos = display_height / 2
    x_change = 0
    y_change = 0
    block_size = 10
    fps = 20
    snakelist = []
    snakeLength = 1
    #gamedisplay.blit(font.render("Score:" + str(snakeLength), True, red), (20, 20))
    AppleX = round(random.randrange(0, display_width-block_size)/10)*10
    AppleY = round(random.randrange(0, display_height-block_size)/10)*10
    while not GameExit:
        while GameOver == True:
            gamedisplay.fill(white)
            screenText("Game Over, press C to play again or Q to quit", black)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        GameExit = True
                        GameOver = False
                    if event.key == pygame.K_c:
                        gameloop()
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                GameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change != block_size:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change != -block_size:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change != block_size:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change != -block_size:
                    y_change = block_size
                    x_change = 0
            if x_pos >= display_width or x_pos <= 0 or y_pos <= 0 or y_pos >= display_height:
                GameOver = True
        x_pos += x_change
        y_pos += y_change
        gamedisplay.fill(white)
        gamedisplay.fill(black, rect=[AppleX, AppleY, block_size, block_size])
        snakehead = []
        snakehead.append(x_pos)
        snakehead.append(y_pos)
        snakelist.append(snakehead)
        if len(snakelist)>snakeLength:
            del snakelist[0]
        for eachSegment in snakelist[:-1]:
            if eachSegment == snakehead:
                GameOver = True
        snake(block_size, snakelist)
        pygame.display.update()
        if x_pos == AppleX and y_pos == AppleY:
            AppleX = round(random.randrange(0, display_width - block_size) / 10) * 10
            AppleY = round(random.randrange(0, display_height - block_size) / 10) * 10
            snakeLength += 1
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()