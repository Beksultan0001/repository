import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Симулятор дождя")

# Цвета
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)

# Настройки капель дождя
NUM_DROPS = 200  # Увеличено количество капель для ускорения
DROPS = [{"x": random.randint(0, WIDTH), "y": random.randint(-HEIGHT, 0), "speed": random.randint(4, 8)} for _ in range(NUM_DROPS)]
DROP_COLOR = LIGHT_BLUE
DROP_WIDTH = 2
DROP_HEIGHT = 10

# Уровень воды
water_level = 0  # Начальный уровень воды
water_rise_rate = 2  # Сколько пикселей уровень воды поднимается за 100 капель
drops_fallen = 0

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

    # Отрисовка воды
    if water_level > 0:
        pygame.draw.rect(screen, BLUE, (0, HEIGHT - water_level, WIDTH, water_level))

    # Обновление капель дождя
    for drop in DROPS:
        drop["y"] += drop["speed"]  # Ускоренное падение капель
        pygame.draw.rect(screen, DROP_COLOR, (drop["x"], drop["y"], DROP_WIDTH, DROP_HEIGHT))

        # Если капля достигла уровня воды или дна экрана
        if drop["y"] >= HEIGHT - water_level:
            drops_fallen += 1
            drop["y"] = random.randint(-20, 0)  # Возвращаем каплю наверх
            drop["x"] = random.randint(0, WIDTH)
            drop["speed"] = random.randint(4, 8)  # Случайная скорость

        # Подъем уровня воды каждые 100 капель
        if drops_fallen >= 100:
            water_level += water_rise_rate
            drops_fallen = 0

    # Ограничение уровня воды
    if water_level >= HEIGHT:
        water_level = HEIGHT

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
