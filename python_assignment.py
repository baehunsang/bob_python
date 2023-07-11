import pygame

SCREEN_WIDTH = 1680
SCREEN_HIEGHT = 960

PADDLE_WIDTH = 100
PADDLE_HIEGHT = 30

PADDLE_X_POS = SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2
PADDLE_Y_POS = SCREEN_HIEGHT - PADDLE_HIEGHT - 100

PADDLE_TO_X = 0 
PADDLE_SPEED = 20

BALL_RADIOUS = 10  

BALL_X_POS = SCREEN_WIDTH // 2  
BALL_Y_POS = SCREEN_HIEGHT - PADDLE_HIEGHT - BALL_RADIOUS - 100  


BALL_TO_X = 10
BALL_TO_Y = 10


BRICK_WIDTH = 100
BRICK_HEIGHT = 30

BRICK_X_POS = 0
BRICK_Y_POS = 0 

class Bricks:
    def __init__(self) -> None:
        self.bricks = self._set_bricks()
    
    def _set_bricks(self):
        bricks = [[] for _ in range(14)]
        for column in range(14):
            for row in range(3):  
                bricks[column].append(pygame.Rect(70 + column * (BRICK_WIDTH + 10), 100 + row * (BRICK_HEIGHT + 10), BRICK_WIDTH, BRICK_HEIGHT))
        return bricks
    
    def draw_brick_into(self, screen):
        for column in range(14):
            for row in range(3):
                if self.bricks[column][row]:  
                    pygame.draw.rect(screen, (127, 127, 127), self.bricks[column][row])
                    self.bricks[column][row].topleft = (70 + column * (BRICK_WIDTH + 10), 100 + row * (BRICK_HEIGHT + 10))


#usage: screen = Screen().set_screen()
class Screen:
    def __init__(self) -> None:
        self.screen_width = SCREEN_WIDTH
        self.screen_hieght = SCREEN_HIEGHT
        self.screen_caption = "BoB python assignment"
    
    def set_screen(self):
        screen = pygame.display.set_mode((self.screen_width, self.screen_hieght))
        pygame.display.set_caption("BoB python assignment")
        return screen


class Game():
    def __init__(self) -> None:
        self.screen = Screen().set_screen()
        self.bricks = Bricks()
        self.fps = pygame.time.Clock()
        
        
    def run(self):
        while True:
            self.bricks.draw_brick_into(self.screen)
            pygame.display.update()

def main():
    pygame.init()

    game = Game()
    game.run()
    pygame.quit()


if __name__ == '__main__':
    main()
