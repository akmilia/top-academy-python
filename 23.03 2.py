# Задание 1
# Напишите программу, которая запрашивает два
# целых числа x и y, после чего вычисляет и выводит
# значение x в степени y. 
x = int(input("X"))
y = int(input("Y")) 
print("result", pow(x, y))
# Задание 2
# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры. 

ars =0
for i in range(100, 999):
    a, b, c =list(ars) 

    if a==b or a==c er b==c
# Задание 3
# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.
# Задание 4
# Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.  




import pygame
import random

SCREEN_WIDTH = 500 # Ширина экрана
SCREEN_HEIGHT = 500 # Высота экрана

PLAYER_WIDTH = SCREEN_WIDTH // 10 # Ширина экрана
PLAYER_HEIGHT = SCREEN_HEIGHT // 10 # Высота экрана
PLAYER_SPEED = PLAYER_HEIGHT // 4

ITEM_WIDTH = SCREEN_WIDTH // 15
ITEM_HEIGHT = SCREEN_HEIGHT // 15

ENEMY_WIDTH = SCREEN_WIDTH // 12

pl_x = (SCREEN_WIDTH // 2) - (PLAYER_WIDTH // 2)
pl_y = (SCREEN_HEIGHT // 2) - (PLAYER_HEIGHT // 2)


E_C = (120, 100, 0)
GREEN   = (0, 15, 30)
RED     = (140, 56, 25)
BLUE    = (34, 100, 210)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MyGame")

pygame.font.init()

# Create a font file by passing font file
# and size of the font 
def text():
    font1 = pygame.font.SysFont('freesanbold.ttf', 50)
    text1 = font1.render('Есть пробитие', True, (0, 255, 0))
    screen.blit(text1, (10, 50))
    
items = []
for i in range(3):
    item_x = random.randint(ITEM_WIDTH, SCREEN_WIDTH - ITEM_WIDTH)
    item_y = random.randint(ITEM_HEIGHT, SCREEN_HEIGHT - ITEM_HEIGHT)
    items.append((item_x, item_y))

enemies = []
for i in range(random.randint(5, 10)):
    enemy_x = random.randint(ITEM_WIDTH, SCREEN_WIDTH - ITEM_WIDTH)
    enemy_y = random.randint(ITEM_HEIGHT, SCREEN_HEIGHT - ITEM_HEIGHT)
    enemies.append((enemy_x, enemy_y))


def draw_player(x, y):
    pygame.draw.rect(screen, RED, [x, y, PLAYER_WIDTH, PLAYER_HEIGHT])

def draw_items(items):
    for item in items:
        pygame.draw.ellipse(screen, BLUE, [item[0], item[1], ITEM_WIDTH, ITEM_HEIGHT])

def draw_enemies(enemies):
    for enemy in enemies:
        pygame.draw.polygon(screen, E_C, [ enemy[0], enemy[1], ENEMY_WIDTH])

def check_collision(items):
    global pl_y
    global pl_x
    for item in items:
        if pl_x < item[0] + ITEM_WIDTH and pl_x + PLAYER_WIDTH > item[0] \
        and pl_y < item[1] + ITEM_HEIGHT and pl_y + PLAYER_HEIGHT > item[1]:
            items.remove(item)
    for enemy in enemies:
        if pl_x < enemy[0] + ENEMY_WIDTH and pl_x + PLAYER_WIDTH > enemy[0] \
        and pl_y < enemy[1] + ENEMY_WIDTH and pl_y + PLAYER_HEIGHT > enemy[1]:
            items.remove(item)


def player_move(diff_x, diff_y) :
    global pl_y
    global pl_x

    new_pl_y = pl_y + diff_y
    if (new_pl_y >= 0 and new_pl_y < SCREEN_HEIGHT):
        pl_y = new_pl_y
    new_pl_x = pl_x + diff_x
    if (new_pl_x >= 0 and new_pl_x < SCREEN_WIDTH):
        pl_x = new_pl_x


def keys_hook(keys):
    if keys[pygame.K_UP]:
        player_move(0, -PLAYER_HEIGHT)
    if keys[pygame.K_DOWN]:
        player_move(0, PLAYER_HEIGHT)
    if keys[pygame.K_LEFT]:
        player_move(-PLAYER_WIDTH, 0)
    if keys[pygame.K_RIGHT]:
        player_move(PLAYER_WIDTH ,0)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

def main_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            keys_hook(pygame.key.get_pressed())
            check_collision(items)
            screen.fill(GREEN)
            draw_player(pl_x, pl_y)
            draw_items(items)
            draw_enemies(enemies)
            pygame.display.update()

            screen.blit(text1, textRect1)

if __name__ == '__main__':
    main_loop()