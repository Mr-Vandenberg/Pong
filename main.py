import pygame
import random
from paddle import Paddle
from ball import Ball

pygame.init() #starts pygame, required

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 74)


size = (800, 600)
gameDisplay = pygame.display.set_mode(size, 0, 32)

# Load the background image for the start screen

# pygame.mixer.music.load("startsongcut.mp3")
# pygame.mixer.music.play(-1)
clock = pygame.time.Clock()


def startScreen():
    # Two different ways to get a message to the screen:
    # Draw an image file to the screen
    background = pygame.image.load("Titlescreen.png")
    gameDisplay.blit(background, (0, 0))

    # Write text to the screen
    text = font.render("Press x to start the game", 1, BLUE)
    gameDisplay.blit(text, (100, 500))

    # Write the image and the text to the screen, in that order
    pygame.display.flip()
    startGame = False

    # Loop that waits for the user to quit the game, or press x to start the game
    while (not startGame):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                    startGame = True


def main():  # main method to run the game
    # define the left paddle, 10 pixels wide, 20 pixels from the left side
    leftPaddle = Paddle(BLUE, 10, 100)
    leftPaddle.rect.x = 20
    leftPaddle.rect.y = 200

    # define the right paddle, 10 pixels wide, 20 pixels from the right side
    rightPaddle = Paddle(BLUE, 10, 100)
    rightPaddle.rect.x = 610
    rightPaddle.rect.y = 200

    # define the ball 10 pixels by 10 pixels starts in the middle of the screen
    ball = Ball(BLACK, 10, 10)
    ball.rect.x = 315
    ball.rect.y = 195

    # This will be a list that will contain all the sprites we intend to use 
    # in our game.
    all_sprites_list = pygame.sprite.Group()

    # Add the paddles and ball to the list of sprites
    all_sprites_list.add(leftPaddle)
    all_sprites_list.add(rightPaddle)
    all_sprites_list.add(ball)

    # Initialise player scores
    game = True
    clock = pygame.time.Clock()

    while game:  # Game loop, takes user input, keeps score
        gameDisplay.fill(WHITE)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return("")
                game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                    game = False
                    return("")
                elif event.key == pygame.K_p:
                  pause = True
                  print ("The game is paused, press i to resume.")
                  while pause:
                    for event in pygame.event.get():
                      if event.key == pygame.K_i:
                        pause = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            leftPaddle.moveUp(5)
        if keys[pygame.K_s]:
            leftPaddle.moveDown(5)
        if keys[pygame.K_UP]:
            rightPaddle.moveUp(5)
        if keys[pygame.K_DOWN]:
            rightPaddle.moveDown(5)

        # Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, leftPaddle) or pygame.sprite.collide_mask(ball, rightPaddle): 
          ball.bounce()

        # --- Game logic should go here
        all_sprites_list.update()

        if ball.rect.x >= 640:
            #ball.velocity[0] = -ball.velocity[0]
            ball.bounce()
        if ball.rect.x <= 0:
            #ball.velocity[0] = -ball.velocity[0]
            ball.bounce()
            
        if ball.rect.y > 400 or ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        # --- Drawing code should go here
        # First, clear the screen to black.
        # Draw the net
        pygame.draw.line(gameDisplay, BLACK, [319, 0], [319, 500], 5)

        # Now let's draw all the sprites in one go. (For now we only have 
        # 2 sprites!)
        all_sprites_list.draw(gameDisplay)

        # Display scores:

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

startScreen()
main()



pygame.quit()
