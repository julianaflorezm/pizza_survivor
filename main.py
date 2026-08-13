import pygame
import random
from dog import Dog
from cat import Cat
from pizza import Pizza
from dealer import Dealer
from interface import Interface
from pizza_box import PizzaBox

# pygame initialization
pygame.init()

# Sounds
pygame.mixer.music.load("font_music.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)  # infinite loop

bang_sound = pygame.mixer.Sound("bang.mp3")
shot_sound = pygame.mixer.Sound("shot.mp3")
loss_life_sound = pygame.mixer.Sound("loss_life.mp3")

bang_sound.set_volume(0.8)
shot_sound.set_volume(0.8)
loss_life_sound.set_volume(0.8)

# Time
initial_time = pygame.time.get_ticks()
final_time = 0

# Game state
PLAYING = "Playing"
FINISHED = "Finished"
game_state = PLAYING
music_stopped = False

# screen creation
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pizza Survivor")
icon = pygame.image.load("pizza.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (800, 600))

# Dealer
dealer = Dealer()

# Interface
interface = Interface()

# Lives
lives = 3
is_invulnerable = False
last_damage_time = -1000
invulnerable_time = 1000  # milliseconds = 1 second
blink_interval = 150

# Life power-up
pizza_box = None
last_pizza_box_time = pygame.time.get_ticks()
pizza_box_interval = random.randint(15000, 20000)
maximum_lives = 5

# Enemies
enemies = []
last_enemy_time = 0
initial_enemy_interval = 3000  # 3 seconds
minimum_enemy_interval = 500   # 0.5 secondss

# Pizza shot
pizza_velocity = 1.0
pizzas = []
last_pizza_time = 0
pizza_interval = 1000  # milliseconds = 1 second

# Score
score = 0

def update_pizza_box(current_time):
    global pizza_box
    global last_pizza_box_time
    global pizza_box_interval
    global lives

    # Crear una caja si no hay una activa
    if pizza_box is None:
        if current_time - last_pizza_box_time >= pizza_box_interval:
            pizza_box = PizzaBox()

    # Revisar la caja que está activa
    if pizza_box is not None:
        # El repartidor recoge la caja
        if dealer.get_rect().colliderect(pizza_box.get_rect()):
            if lives < maximum_lives:
                lives += 1

            pizza_box = None
            last_pizza_box_time = current_time
            pizza_box_interval = random.randint(15000, 20000)

        # La caja desaparece después de cinco segundos
        elif pizza_box.has_expired(current_time):
            pizza_box = None
            last_pizza_box_time = current_time
            pizza_box_interval = random.randint(15000, 20000)

def get_enemy_interval(current_time):
    elapsed_time = get_elapsed_time(current_time)

    # Reduce 250 ms cada 10 secs.
    reduction = (elapsed_time // 10000) * 250

    return max(
        minimum_enemy_interval,
        initial_enemy_interval - reduction
    )


def get_elapsed_time(current_time):
    if game_state == FINISHED:
        return final_time - initial_time

    return current_time - initial_time


def create_enemy():
    enemy_class = random.choice([Dog, Cat])
    enemies.append(enemy_class())


def move_dealer():
    dealer.move()


def move_enemies():
    for enemy in enemies:
        enemy.move_towards(dealer.x, dealer.y)


def check_enemy_collision(current_time):
    global lives, enemies, is_invulnerable, last_damage_time

    if is_invulnerable:
        return

    dealer_rect = dealer.get_rect()
    new_enemies = []
    lost_life = False

    for enemy in enemies:
        enemy_rect = enemy.get_rect()

        if dealer_rect.colliderect(enemy_rect) and not lost_life:
            lives -= 1
            loss_life_sound.play()
            is_invulnerable = True
            last_damage_time = current_time
            lost_life = True
        else:
            new_enemies.append(enemy)

    enemies = new_enemies


def update_invulnerability(current_time):
    global is_invulnerable, game_state

    if is_invulnerable and current_time - last_damage_time >= invulnerable_time:
        is_invulnerable = False

    if game_state == FINISHED and is_invulnerable:
        is_invulnerable = False


def update_game_state(current_time):
    global game_state, final_time, music_stopped

    if lives <= 0 and game_state == PLAYING:
        game_state = FINISHED
        final_time = current_time

    if game_state == FINISHED and not music_stopped:
        pygame.mixer.music.stop()
        music_stopped = True

    update_invulnerability(0)


def get_nearest_enemy():
    if len(enemies) == 0:
        return None

    nearest_enemy = enemies[0]
    nearest_distance = nearest_enemy.distance_to(dealer.x, dealer.y)

    for enemy in enemies:
        distance = enemy.distance_to(dealer.x, dealer.y)

        if distance < nearest_distance:
            nearest_distance = distance
            nearest_enemy = enemy

    return nearest_enemy


def shoot_pizza():
    target_enemy = get_nearest_enemy()

    if target_enemy is None:
        return

    # Center of dealer and enemy, so the pizza travels more naturally
    pizza_x = dealer.get_center_x() - 16
    pizza_y = dealer.get_center_y() - 16
    target_x = target_enemy.get_center_x()
    target_y = target_enemy.get_center_y()

    dx = target_x - pizza_x
    dy = target_y - pizza_y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if distance > 0:
        pizza_change_x = (dx / distance) * pizza_velocity
        pizza_change_y = (dy / distance) * pizza_velocity
        pizzas.append(Pizza(pizza_x, pizza_y, pizza_change_x, pizza_change_y))
        bang_sound.play()


def move_pizzas():
    global pizzas

    for pizza_data in pizzas:
        pizza_data.move()

    pizzas = [
        pizza_data
        for pizza_data in pizzas
        if pizza_data.is_inside_screen()
    ]


def check_pizza_enemy_collisions():
    global pizzas, enemies, lives, score

    pizzas_to_keep = []
    enemies_killed = 0

    for pizza_data in pizzas:
        pizza_rect = pizza_data.get_rect()
        pizza_hit_enemy = False

        for enemy in enemies:
            enemy_rect = enemy.get_rect()

            if pizza_rect.colliderect(enemy_rect):
                enemy.receive_damage()

                if enemy.is_dead():
                    enemies_killed += 1
                    score += 1
                    shot_sound.play()

                pizza_hit_enemy = True
                break

        if not pizza_hit_enemy:
            pizzas_to_keep.append(pizza_data)

    pizzas = pizzas_to_keep

    enemies = [
        enemy
        for enemy in enemies
        if not enemy.is_dead()
    ]

    lives += enemies_killed


def handle_events():
    global its_exec

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            its_exec = False

        if game_state != PLAYING:
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dealer.move_left()
            if event.key == pygame.K_RIGHT:
                dealer.move_right()
            if event.key == pygame.K_UP:
                dealer.move_up()
            if event.key == pygame.K_DOWN:
                dealer.move_down()

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                dealer.stop_horizontal()
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                dealer.stop_vertical()


def update_playing(current_time):
    global last_enemy_time, last_pizza_time

    move_dealer()
    update_pizza_box(current_time)

    enemy_interval = get_enemy_interval(current_time)

    # Create enemies increasingly faster
    if current_time - last_enemy_time >= enemy_interval:
        create_enemy()
        last_enemy_time = current_time

    # Shoot one pizza every second toward the nearest enemy
    if current_time - last_pizza_time >= pizza_interval:
        shoot_pizza()
        last_pizza_time = current_time

    # Update game objects
    move_enemies()
    move_pizzas()

    # Collisions
    check_pizza_enemy_collisions()
    check_enemy_collision(current_time)
    update_invulnerability(current_time)
    update_game_state(current_time)


def draw_game(current_time):
    screen.blit(background, (0, 0))

    if not is_invulnerable or (current_time // blink_interval) % 2 == 0:
        dealer.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    for pizza_data in pizzas:
        pizza_data.draw(screen)

    if pizza_box is not None:
        pizza_box.draw(screen)

    interface.draw_lives(screen, lives)
    interface.draw_score(screen, score)
    interface.draw_timer(screen, get_elapsed_time(current_time))

    if game_state == FINISHED:
        interface.draw_end_screen(
            screen,
            score,
            final_time - initial_time
        )

    pygame.display.update()


# First enemy at the beginning of the game
create_enemy()

# game loop
its_exec = True
while its_exec:
    current_time = pygame.time.get_ticks()

    handle_events()

    if game_state == PLAYING:
        update_playing(current_time)
    else:
        update_game_state(current_time)

    draw_game(current_time)

pygame.quit()
