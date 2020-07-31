import random
from config import Config
from snake import Snake
from apple import Apple
import pygame, sys

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption("Snaky")
        self.apple = Apple()
        self.snake = Snake()

    def drawGrid(self):
        for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):
            pygame.draw.line(self.screen, Config.DARKGRAY, (x, 0), (x, Config.WINDOW_HEIGHT))
        for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
            pygame.draw.line(self.screen, Config.DARKGRAY, (0, y), (Config.WINDOW_WIDTH, y))

    def drawSnake(self):
        for coord in self.snake.wormCoords:
            x = coord['x'] * Config.CELLSIZE
            y = coord['y'] * Config.CELLSIZE
            snakeSegmentRect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
            pygame.draw.rect(self.screen, Config.DARKGREEN, snakeSegmentRect)
            snakeInnerSegmentRect = pygame.Rect(x+4, y+4, Config.CELLSIZE - 8, Config.CELLSIZE - 8 )
            pygame.draw.rect(self.screen, Config.GREEN, snakeInnerSegmentRect)

    def drawApple(self):
        x = self.apple.x * Config.CELLSIZE
        y = self.apple.y * Config.CELLSIZE
        appleSegRect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
        pygame.draw.rect(self.screen,  Config.RED, appleSegRect)
    def drawScore(self, score):
        scoreSurf = self.BASICFONT.render('Score:  %s' % (score), True, Config.WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (Config.WINDOW_WIDTH - 120, 10)
        self.screen.blit(scoreSurf, scoreRect)
        
    def draw(self):
        self.screen.fill(Config.BG_COLOR)
        self.drawGrid()
        self.drawSnake()
        self.drawApple()
        self.drawScore(len(self.snake.wormCoords) - 3)
        pygame.display.update()
        self.clock.tick(Config.FPS)

    def handleKeyEvents(self, event):
        if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.direction!=self.snake.RIGHT:
            self.snake.direction = self.snake.LEFT
        elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.snake.direction!=self.snake.LEFT:
            self.snake.direction = self.snake.RIGHT
        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.direction != self.snake.UP:
                self.snake.direction = self.snake.DOWN
        elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.snake.direction != self.snake.DOWN:
            self.snake.direction = self.snake.UP
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()

    def resetGame(self):
        del self.snake
        del self.apple
        self.snake = Snake()
        self.apple = Apple()
        return True

    def isGameOver(self):
        if(self.snake.wormCoords[self.snake.HEAD]['x'] == -1 or self.snake.wormCoords[self.snake.HEAD]['x'] == Config.CELLWIDTH or self.snake.wormCoords[self.snake.HEAD]['y'] == -1 or self.snake.wormCoords[self.snake.HEAD]['y'] == Config.CELLHEIGHT):
            return self.resetGame()
        for wormBody in self.snake.wormCoords[1:]:
            if wormBody['x'] == self.snake.wormCoords[self.snake.HEAD]['x'] and wormBody['y'] == self.snake.wormCoords[self.snake.HEAD]['y']:
                return self.resetGame()
    def drawPressKey(self):
        pressKeySurf = self.BASICFONT.render('Press a key to start', True, Config.DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (Config.WINDOW_WIDTH - 200, Config.WINDOW_HEIGHT - 30)
        self.screen.blit(pressKeySurf, pressKeyRect)
    def checkForKey(self):
        if len(pygame.event.get(pygame.QUIT)) > 0:
            pygame.quit()
        keyUp = pygame.event.get(pygame.KEYUP)
        if len(keyUp) == 0:
            return None
        if keyUp[0].key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
        return keyUp[0].key
    def displayGameOver(self):
        gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
        gameOverSurf = gameOverFont.render('Game Over', True, Config.WHITE)
        gameRect = gameOverSurf.get_rect()
        gameRect.midtop = (Config.WINDOW_WIDTH/2, Config.WINDOW_HEIGHT/2)
        self.screen.blit(gameOverSurf, gameRect)
        self.drawPressKey()
        pygame.display.update()
        pygame.time.wait(500)
        self.checkForKey()
        while True:
            if self.checkForKey():
                pygame.event.get()
                return
    def run(self):
        while True:
            self.gameLoop()
            self.displayGameOver()

    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.handleKeyEvents(event)

            self.snake.update(self.apple)
            self.draw()
            if self.isGameOver():
                break



