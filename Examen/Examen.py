import pygame
import random
import sys

# Configuración de la pantalla
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Aventura y Estrategia")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fuente
font = pygame.font.SysFont("Arial", 24)

# Variables del juego
player_health = 100
difficulty = 1
player_score = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))
        self.health = player_health

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

    def upgrade(self):
        self.health += 20  # Aumentar salud al subir de nivel

class Enemy(pygame.sprite.Sprite):
    def __init__(self, difficulty):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(0, screen_width), random.randint(0, screen_height)))
        self.health = 50 * difficulty

    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += 1
        if self.rect.x > player.rect.x:
            self.rect.x -= 1
        if self.rect.y < player.rect.y:
            self.rect.y += 1
        if self.rect.y > player.rect.y:
            self.rect.y -= 1

def draw_health_bar(health, x, y):
    pygame.draw.rect(screen, RED, (x, y, 50, 10))
    pygame.draw.rect(screen, GREEN, (x, y, 50 * (health / 100), 10))

def show_game_status(player):
    draw_health_bar(player.health, 10, 10)
    score_text = font.render(f"Puntaje: {player_score}", True, WHITE)
    screen.blit(score_text, (10, 30))
    for enemy in enemies:
        draw_health_bar(enemy.health, enemy.rect.x, enemy.rect.y - 20)

def show_menu():
    screen.fill(BLACK)
    title_text = font.render("Juego de Aventura y Estrategia", True, WHITE)
    start_text = font.render("Empezar", True, WHITE)
    instructions_text = font.render("Instrucciones", True, WHITE)
    scores_text = font.render("Puntajes", True, WHITE)

    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 4))
    screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, screen_height // 2))
    screen.blit(instructions_text, (screen_width // 2 - instructions_text.get_width() // 2, screen_height // 2 + 40))
    screen.blit(scores_text, (screen_width // 2 - scores_text.get_width() // 2, screen_height // 2 + 80))

    pygame.display.flip()

def game_over():
    screen.fill(BLACK)
    over_text = font.render("¡Has perdido!", True, WHITE)
    screen.blit(over_text, (screen_width // 2 - over_text.get_width() // 2, screen_height // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

def level_up(player):
    player.upgrade()  # Mejora las estadísticas del jugador
    return 10  # Retorna 10 puntos al subir de nivel

def game_loop():
    global difficulty, player_health, player_score
    player = Player()
    all_sprites.add(player)

    for _ in range(3):  # Crear 3 enemigos al inicio
        enemy = Enemy(difficulty)
        enemies.add(enemy)
        all_sprites.add(enemy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Actualizar el jugador
        player.update()

        # Actualizar enemigos
        for enemy in enemies:
            enemy.update(player)  # Pasar el jugador a los enemigos para actualizar

        # Colisiones
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                player.health -= 1  # El jugador recibe daño

        # Verificar si se presiona X para atacar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:  # Al presionar X
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    enemy.health -= 10  # El enemigo recibe daño al ser atacado
                    if enemy.health <= 0:
                        enemy.kill()
                        player_score += 10  # Incrementar puntaje por cada enemigo derrotado

        if player.health <= 0:
            game_over()
            return  # Regresar al menú después de perder

        if len(enemies) == 0:
            difficulty += 1  # Aumentar la dificultad
            player_score += level_up(player)  # Aumentar puntaje y mejorar estadísticas
            for _ in range(difficulty + 2):  # Aumentar el número de enemigos
                enemy = Enemy(difficulty)
                enemies.add(enemy)
                all_sprites.add(enemy)

        # Dibujar todo
        screen.fill(BLACK)
        all_sprites.draw(screen)
        show_game_status(player)  # Pasar el jugador a la función
        pygame.display.flip()
        pygame.time.delay(50)

# Grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Mostrar el menú al inicio
show_menu()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo
                mouse_pos = event.pos
                if (screen_width // 2 - 60 < mouse_pos[0] < screen_width // 2 + 60 and
                        screen_height // 2 - 20 < mouse_pos[1] < screen_height // 2 + 20):
                    game_loop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_loop()

    pygame.display.flip()
