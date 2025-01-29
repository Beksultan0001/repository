import pygame
import random
import math

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мерцающие звезды")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Параметры звёзд
NUM_STARS = 150  # Количество звёзд
STARS = [
    {
        "x": random.randint(0, WIDTH),               # Координаты звезды
        "y": random.randint(0, HEIGHT),
        "base_radius": random.randint(2, 4),         # Базовый радиус звезды
        "radius": 0,                                 # Текущий радиус (меняется)
        "speed": random.uniform(0.02, 0.05),         # Скорость мерцания
        "phase": random.uniform(0, 2 * math.pi),     # Сдвиг фазы (для разного старта)
    }
    for _ in range(NUM_STARS)
]

# FPS
clock = pygame.time.Clock()
FPS = 60

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(BLACK)

    # Обновление и отрисовка звёзд
    for star in STARS:
        # Анимация мерцания (радиус меняется плавно с синусом)
        star["radius"] = star["base_radius"] + math.sin(pygame.time.get_ticks() * star["speed"] + star["phase"]) * 2

        # Отрисовка звезды
        pygame.draw.circle(screen, WHITE, (star["x"], star["y"]), max(1, int(star["radius"])))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
