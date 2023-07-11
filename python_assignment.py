import pygame

SCREEN_WIDTH = 1000
SCREEN_HIEGHT = 800

PADDLE_WIDTH = 100
PADDLE_HIEGHT = 30

PADDLE_X_POS = SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2
PADDLE_Y_POS = SCREEN_HIEGHT - PADDLE_HIEGHT - 100

PADDLE_SPEED = 20

BALL_RADIOUS = 10  

BALL_X_POS = SCREEN_WIDTH // 2  
BALL_Y_POS = SCREEN_HIEGHT - PADDLE_HIEGHT - BALL_RADIOUS - 100  


BALL_TO_X = 10
BALL_TO_Y = 10


BRICK_WIDTH = SCREEN_WIDTH // 14 - 10
BRICK_HEIGHT = SCREEN_HIEGHT // 20 - 10

BRICK_X_POS = 0
BRICK_Y_POS = 0 

MARGIN_X = 45
MARGIN_Y = 10

ROW = 3
COL = 14

class Paddle:
    def __init__(self) -> None:
        self.paddle_x_pos = PADDLE_X_POS
        self.paddle_y_pos = PADDLE_Y_POS
        self.paddle = pygame.Rect(self.paddle_x_pos, self.paddle_y_pos, PADDLE_WIDTH, PADDLE_HIEGHT)
        self.paddle_diff_x = 0 

    def move_paddle_left(self):
        self.paddle_diff_x -= PADDLE_SPEED

    def move_paddle_right(self):
        self.paddle_diff_x += PADDLE_SPEED

    def stop_paddle(self):
        self.paddle_diff_x = 0

    def update_paddle_pos(self):
        self.paddle_x_pos += self.paddle_diff_x

        if self.paddle_x_pos < 0:  
            self.paddle_x_pos = 0
        elif self.paddle_x_pos + PADDLE_WIDTH > SCREEN_WIDTH:  
            self.paddle_x_pos = SCREEN_WIDTH - PADDLE_WIDTH
        self.paddle = pygame.Rect(self.paddle_x_pos, self.paddle_y_pos, PADDLE_WIDTH, PADDLE_HIEGHT)

    def draw_paddle_into(self, screen):
        self.update_paddle_pos()
        pygame.draw.rect(screen, (0, 255, 255), self.paddle)





class Bricks:
    def __init__(self) -> None:
        self.bricks = self._set_bricks()
    
    def _set_bricks(self):
        bricks = [[] for _ in range(COL)]
        for column in range(COL):
            for row in range(ROW):  
                bricks[column].append(pygame.Rect(MARGIN_X + column * (BRICK_WIDTH + 5), MARGIN_Y + row * (BRICK_HEIGHT + 5), BRICK_WIDTH, BRICK_HEIGHT))
        return bricks
    
    def draw_brick_into(self, screen):
        for column in range(COL):
            for row in range(ROW):
                if self.bricks[column][row]:  
                    pygame.draw.rect(screen, (127, 127, 127), self.bricks[column][row])
                    self.bricks[column][row].topleft = (MARGIN_X + column * (BRICK_WIDTH + 5), MARGIN_Y + row * (BRICK_HEIGHT + 5))


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
        self.paddle = Paddle()
        self.fps = pygame.time.Clock()
        self.is_game_running = True
        
    def run(self):
        while self.is_game_running:
            self.dt = self.fps.tick(60)
            self.manage_event()
            

            self.screen.fill((0, 0, 35))
            self.bricks.draw_brick_into(self.screen)
            self.paddle.draw_paddle_into(self.screen)
            pygame.display.update()

    def manage_event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.paddle.move_paddle_left()
                elif event.key == pygame.K_RIGHT:
                    self.paddle.move_paddle_right()
                elif event.key == pygame.K_ESCAPE:  
                    self.is_game_running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  
                    self.paddle.stop_paddle()

def main():
    pygame.init()

    game = Game()
    game.run()
    pygame.quit()


if __name__ == '__main__':
    main()
