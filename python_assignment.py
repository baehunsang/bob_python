import pygame

SCREEN_WIDTH = 1000
SCREEN_HIEGHT = 800

PADDLE_WIDTH = 150
PADDLE_HIEGHT = 30

PADDLE_X_POS = SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2
PADDLE_Y_POS = SCREEN_HIEGHT - PADDLE_HIEGHT - 100

PADDLE_SPEED = 20

BALL_RADIOUS = 10  

BALL_X_POS = SCREEN_WIDTH // 2  
BALL_Y_POS = SCREEN_HIEGHT - PADDLE_HIEGHT - BALL_RADIOUS - 120 

#속도 벡터
BALL_TO_X = -8
BALL_TO_Y = -7


BRICK_WIDTH = SCREEN_WIDTH // 14 - 10
BRICK_HEIGHT = SCREEN_HIEGHT // 20 - 10

BRICK_X_POS = 0
BRICK_Y_POS = 0 

MARGIN_X = 45
MARGIN_Y = 10

ROW = 3
COL = 14



class Ball:
    def __init__(self) -> None:
        self.ball_x_pos = BALL_X_POS
        self.ball_y_pos = BALL_Y_POS
        self.ball = pygame.Rect(self.ball_x_pos, self.ball_y_pos, BALL_RADIOUS * 2, BALL_RADIOUS * 2)


        self.ball_to_x = BALL_TO_X
        self.ball_to_y = BALL_TO_Y

    def manage_frame_collision(self):
        if self.ball_x_pos - BALL_RADIOUS <= 0:  
            self.ball_to_x = -self.ball_to_x
        elif self.ball_x_pos + BALL_RADIOUS >= SCREEN_WIDTH:  
            self.ball_to_x = -self.ball_to_x

        if self.ball_y_pos - BALL_RADIOUS <= 0:  
            self.ball_to_y = -self.ball_to_y

    def is_game_over(self):
        return self.ball_y_pos + BALL_RADIOUS >= SCREEN_HIEGHT

    def update_ball_pos(self):
        self.manage_frame_collision()
        self.ball_x_pos += self.ball_to_x
        self.ball_y_pos += self.ball_to_y
        self.ball = pygame.Rect(self.ball_x_pos, self.ball_y_pos, BALL_RADIOUS * 2, BALL_RADIOUS * 2)
        self.ball.center = (self.ball_x_pos - 10, self.ball_y_pos - 10) 

    def ball_after_collision(self):
        self.ball_to_y = -self.ball_to_y

    def draw_ball_into(self, screen):
        self.update_ball_pos()
        pygame.draw.circle(screen, (0, 0, 255), (self.ball_x_pos, self.ball_y_pos), 10)

    def get_ball(self):
        return self.ball





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

    def get_paddle(self):
        return self.paddle
    




class Bricks:
    def __init__(self) -> None:
        self.bricks = self._set_bricks()
        self.group = pygame.sprite.Group()
    
    def _set_bricks(self):
        bricks = [[] for _ in range(COL)]
        for column in range(COL):
            for row in range(ROW):
                brick = pygame.Rect(MARGIN_X + column * (BRICK_WIDTH + 5), MARGIN_Y + row * (BRICK_HEIGHT + 5), BRICK_WIDTH, BRICK_HEIGHT)
                bricks[column].append([brick, 1])
        return bricks
    
    def draw_brick_into(self, screen):
        for column in range(COL):
            for row in range(ROW):
                if self.bricks[column][row][1]:  
                    pygame.draw.rect(screen, (127, 127, 127), self.bricks[column][row][0])
                    self.bricks[column][row][0].topleft = (MARGIN_X + column * (BRICK_WIDTH + 5), MARGIN_Y + row * (BRICK_HEIGHT + 5))

    def get_bricks(self, column, row):
        return self.bricks[column][row][0]
    
    def delete_brick(self, column, row):
        self.bricks[column][row][1] = 0
        self.bricks[column][row][0] = None

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
        self.ball = Ball()
        self.fps = pygame.time.Clock()
        self.is_game_running = True
    def run(self):
        while self.is_game_running:
            self.dt = self.fps.tick(60)
            self.manage_event()
            

            self.screen.fill((0, 0, 35))
            self.manage_ball_paddle_collision()
            self.manage_ball_brick_collision()
            self.ball.draw_ball_into(self.screen)
            self.bricks.draw_brick_into(self.screen)
            self.paddle.draw_paddle_into(self.screen)
            self.manage_game_end_condition()
            if self.ball.is_game_over():
                font = pygame.font.SysFont(None, 100)  
                text = font.render("GAME OVER...", True, (255, 255, 255)) 
                text_width = text.get_rect().size[0]  
                text_height = text.get_rect().size[1]
                text_x_pos = SCREEN_WIDTH // 2 - text_width // 2 
                text_y_pos = SCREEN_HIEGHT // 2 - text_height // 2
                self.screen.blit(text, (text_x_pos, text_y_pos))
                pygame.display.update()
                pygame.time.delay(1000)
                self.is_game_running = False
                continue
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

    def manage_ball_paddle_collision(self):
        if self.ball.get_ball().colliderect(self.paddle.get_paddle()):
            self.ball.ball_after_collision()


    def manage_ball_brick_collision(self):
        for colmn in range(COL):
            for row in range(ROW):
                if(self.bricks.get_bricks(colmn,row)):
                    if self.ball.get_ball().colliderect(self.bricks.get_bricks(colmn,row)):
                        self.ball.ball_after_collision()
                        self.bricks.delete_brick(colmn, row)
                        return
                    
    def manage_game_end_condition(self):
        for colmn in range(COL):
            for row in range(ROW):
                if(self.bricks.get_bricks(colmn,row)):
                    return
        font = pygame.font.SysFont(None, 100)  
        text = font.render("GAME CLEAR!!", True, (255, 255, 255)) 
        text_width = text.get_rect().size[0]  
        text_height = text.get_rect().size[1]
        text_x_pos = SCREEN_WIDTH // 2 - text_width // 2 
        text_y_pos = SCREEN_HIEGHT // 2 - text_height // 2
        self.screen.blit(text, (text_x_pos, text_y_pos))
        pygame.display.update()
        pygame.time.delay(1000)
        self.is_game_running = False



def main():
    pygame.init()

    game = Game()
    game.run()
    pygame.quit()


if __name__ == '__main__':
    main()
