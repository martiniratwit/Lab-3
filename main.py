# Git repo (add prof.memo), add main function, picture of pong, requirments.txt
import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 480

pygame.display.set_caption("lab 3")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()

leftwall = pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0, 0), (20, HEIGHT)))
topwall = pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0, 0), (WIDTH, 20)))
bottomwall = pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0, 460), (WIDTH, 20)))


class Ball():
    xPos = 400
    yPos = 240

    xVelocity = [1,-1][random.randint(0,1)] * .4
    yVelocity = [1,-1][random.randint(0,1)]* .4

    def move(self,screen):
        pygame.draw.circle(screen, pygame.Color("black"),(self.xPos, self.yPos),10)
        self.xPos += self.xVelocity
        self.yPos += self.yVelocity
        pygame.draw.circle(screen, pygame.Color("white"),(self.xPos, self.yPos),10)

ball = Ball()

def ballCollision():

    if ball.xPos >= 20:
        ball.xVelocity *= -1
    if ball.xPos <= WIDTH:
        ball.xVelocity *= -1
    if ball.yPos >= topwall.bottom:
        ball.yVelocity *= -1
    if ball.yPos <= bottomwall.top:
        ball.yVelocity *= -1

def main():
    running = True
    while running:
        # event handling, gets all event from the event queue
        pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0, 0), (20, HEIGHT)))
        pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0, 0), (WIDTH, 20)))
        pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0, 460), (WIDTH, 20)))
        pygame.display.update()
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        ballCollision()
        ball.move(screen)
        pygame.display.flip()

# define a variable to control the main loop



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()