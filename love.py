import pygame
import random
import math

# 初始化 pygame
pygame.init()

# 窗口设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("世水长流 直到永远 ❤️")

# 颜色定义
BLACK = (0, 0, 0)
PINK = (255, 143, 171)
RED_PINK = (255, 92, 141)

# 爱心类（自动漂浮）
class Heart:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = HEIGHT + 10
        self.speed = random.uniform(1, 3)
        self.size = random.randint(8, 16)
        self.opacity = 0

    def update(self):
        self.y -= self.speed
        self.x += math.sin(self.y * 0.01) * 1.5
        if self.opacity < 255:
            self.opacity += 8

    def draw(self):
        if self.opacity > 0:
            self.draw_heart(screen, PINK, (self.x, self.y), self.size, self.opacity)

    def draw_heart(self, surface, color, pos, size, opacity):
        x, y = pos
        surface.set_alpha(opacity)
        pygame.draw.circle(surface, color, (x - size//2, y), size//2)
        pygame.draw.circle(surface, color, (x + size//2, y), size//2)
        pygame.draw.polygon(surface, color, [
            (x - size, y),
            (x + size, y),
            (x, y + size)
        ])

# 烟花爱心类（点击爆炸）
class Firework:
    def __init__(self, x, y):
        self.particles = []
        for _ in range(12):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(2, 5)
            self.particles.append({
                "x": x,
                "y": y,
                "vx": math.cos(angle) * speed,
                "vy": math.sin(angle) * speed,
                "size": random.randint(4, 8),
                "life": 100
            })

    def update(self):
        alive = []
        for p in self.particles:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["life"] -= 4
            if p["life"] > 0:
                alive.append(p)
        self.particles = alive

    def draw(self):
        for p in self.particles:
            heart.draw_heart(screen, RED_PINK, (p["x"], p["y"]), p["size"], p["life"])

# 文字渲染（改用系统字体，避免文件找不到）
font = pygame.font.SysFont("simhei", 50)  # 系统黑体，无需单独文件
text = font.render("世水长流 直到永远", True, (255, 255, 255))
text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))

# 主程序
hearts = []
fireworks = []
clock = pygame.time.Clock()
heart = Heart()  # 实例化用于调用 draw_heart 方法

# 自动生成爱心
pygame.time.set_timer(pygame.USEREVENT, 120)

# 主循环
running = True
while running:
    screen.fill(BLACK)
    screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 自动飘爱心
        if event.type == pygame.USEREVENT:
            hearts.append(Heart())
        # 点击 = 烟花
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            fireworks.append(Firework(x, y))

    # 更新并画爱心
    for heart in hearts[:]:
        heart.update()
        heart.draw()
        if heart.y < -20:
            hearts.remove(heart)

    # 更新并画烟花
    for fw in fireworks[:]:
        fw.update()
        fw.draw()
        if not fw.particles:
            fireworks.remove(fw)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()