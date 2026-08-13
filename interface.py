import pygame


class Interface:
    def __init__(self):
        self.heart_width = 32
        self.heart_height = 32
        self.heart_image = pygame.image.load("heart.png")
        self.heart_image = pygame.transform.scale(
            self.heart_image,
            (self.heart_width, self.heart_height)
        )

        self.font_score = pygame.font.SysFont(None, 36, bold=True)
        self.font_timer = pygame.font.SysFont(None, 36, bold=True)
        self.font_game_over = pygame.font.SysFont(None, 90, bold=True)
        self.font_end_info = pygame.font.SysFont(None, 42, bold=True)

    def format_time(self, milliseconds):
        total_seconds = milliseconds // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:02d}"

    def draw_lives(self, screen_surface, lives):
        for i in range(lives):
            screen_surface.blit(self.heart_image, (10 + i * 36, 10))

    def draw_score(self, screen_surface, score):
        score_text = self.font_score.render(
            f"Score: {score}",
            True,
            (255, 255, 255)
        )
        screen_surface.blit(score_text, (650, 10))

    def draw_timer(self, screen_surface, elapsed_time):
        timer_text = self.font_timer.render(
            f"Tiempo {self.format_time(elapsed_time)}",
            True,
            (255, 255, 255)
        )
        screen_surface.blit(timer_text, (400 - timer_text.get_width() // 2, 10))

    def draw_end_screen(self, screen_surface, score, survived_time):
        game_over_text = self.font_game_over.render(
            "GAME OVER",
            True,
            (255, 255, 255)
        )
        score_text = self.font_end_info.render(
            f"Puntaje final: {score}",
            True,
            (255, 255, 255)
        )
        time_text = self.font_end_info.render(
            f"Tiempo sobrevivido: {self.format_time(survived_time)}",
            True,
            (255, 255, 255)
        )

        screen_surface.blit(game_over_text, (400 - game_over_text.get_width() // 2, 210))
        screen_surface.blit(score_text, (400 - score_text.get_width() // 2, 310))
        screen_surface.blit(time_text, (400 - time_text.get_width() // 2, 360))
