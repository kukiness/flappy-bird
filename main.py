import pygame as pg
import random
import sys

DISPLAY_W = 400
DISPLAY_H = 500
DISPLAY = pg.display.set_mode((DISPLAY_W, DISPLAY_H))
pg.display.set_caption("FLAPPY BIRD")
FPS = 30
FPS_CLOCK = pg.time.Clock()

class Bird:
    def __init__(self):
        self.x = 120
        self.y = 200
        self.img_list = [pg.image.load("../textures/0.png"),
                         pg.image.load("../textures/1.png"),
                         pg.image.load("../textures/2.png"),
                         pg.image.load("../textures/dead.png")]
        self.num_img = 0
        self._gravity = 0
    def try_jump(self):
        jump_border = 25
        if self.y > jump_border:
            self.y -= 30
            self._gravity = -4
            self.num_img = 1
    def fall(self):
        if self.gravity < 0:
            self.num_img = 2
        else:
            self.num_img = 0
        self.y += self._gravity
        self._gravity += 0.32
    def check_bird_outside_window(self):
        if self.y > DISPLAY_H:
            return True
        else:
            return False


class Columns:
    def __int__(self, x, y, bottom_column):
        self.x = x
        self.y = y
        self.height = 320
        self.width = 52
        self.img = pg.image.load("../textures/pipe-green.png")
        if not bottom_column:
            self.img = pg.transform.flip(self.img, 0, 1)

class WorkWithColumns:
    def __init__(self):
        self.columns_list = []
        self._space_between_column
        self._def_columns_x_pos = DISPLAY_W
        self._column_move_speed = 2

    def create_new_pair_columns:
        column_up_y = random.randint(-220, 0) #длина минус аекватные 100 пикселей
        column_bottom_y =320 + column_up_y + self._space_between_column
        self.columns_list.append(column_up)
        self.columns_list.append(columns_work)
        self._delete_pair_columns()
    def _delete_pair_columns(self):
        for column in self.columns_list:
            if column.x < -column.width:
                self.columns_list.remove(column)
    def columns_move:
        for column in self.columns_list:
            column.x -= 2
    def check_collision_with_bird(self, bird_x, bird_y, bird_w, bird_h):
        bird = pg.Rect(bird_x, bird_y, bird_w, bird_h)
        for column in self.columns_list:
            column_rect = column.img.get_rect()
            column_rect.x = column.x
            column_rect.y = column.y
            if bird.colliderect(column_rect):
                return True

def finish():
    pg.quit()
    sys.exit(0)

def check_continue_game(bird, columns_work):
    if not bird.check_bird_outside_window():
        return True
    else:
        return False

def main():
    bg = pg.image.load("../textures/background.jpg")
    #column = Column()
    bird = Bird()
    pg.time.set_timer(pygame.USEREVENT, 1000)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish()
            elif event.type == pg.KEY_DOWN:
                if event.key == pg.KEY_SPACE:
                    bird.try_jump()
            elif event.type == pg.USEREVENT:
                columns_work.create_new_pair_columns()

        bird.fall()
        columns_work.columns_move()
        DISPLAY.blit(bg, (0, 0))
        DISPLAY.blit(bird.img_list[bird.num_img], (bird.x, bird.y))
        for column in columns_work.columns_list:
            DISPLAY.blit(column.img, (column.x, column.y))
        pg.display.update()
        FPS_CLOCK.tick(FPS)


if __name__ == '__main__':
    main()






