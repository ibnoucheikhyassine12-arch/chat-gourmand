import pygame
from player import Player
from objective import Objective
from bombe import Bombe
from database import creer_table, ajouter_score, meilleur_score
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SPEED_INCREASE, PLAYER_LIVES, HEART_SIZE


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("chat-gourmand")

        self.running = True
        self.started = False
        self.game_over = False

        self.player = Player()
        self.objective = Objective()
        self.bombe = Bombe()

        self.score = 0
        self.lives = PLAYER_LIVES
        self.font = pygame.font.SysFont("impact", 30)
        self.font_titre = pygame.font.SysFont("impact", 60)

        # créer la table et lire le meilleur score
        creer_table()
        self.best_score = meilleur_score()

        # charger l'image du coeur
        self.heart_image = pygame.image.load("assets/heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (HEART_SIZE, HEART_SIZE))

    def keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_LEFT]:
            self.player.move_left()

    def end_game(self):
        # fin de partie : enregistrer le score dans la base
        self.game_over = True
        ajouter_score(self.score)
        self.best_score = max(self.best_score, meilleur_score())

    def check_collision(self):
        # le chat touche le poisson : +100 points, le jeu accélère
        if self.player.rect.colliderect(self.objective.rect):
            self.objective.respawn()
            self.score += 100
        if self.score > self.best_score:
            self.best_score = self.score
            self.objective.speed += SPEED_INCREASE
            self.bombe.speed += SPEED_INCREASE

        # le chat touche la bombe : -1 vie
        if self.player.rect.colliderect(self.bombe.rect):
            self.lives -= 1
            self.bombe.respawn()
            if self.lives <= 0:
                self.end_game()

    def draw_home(self):
        # écran d'accueil
        self.screen.fill((135, 206, 235))

        titre = self.font_titre.render("CHAT GOURMAND", True, (255, 255, 255))
        regles = self.font.render("Attrape les poissons, évite les bombes", True, (255, 255, 255))
        record = self.font.render(f"Meilleur score : {self.best_score}", True, (255, 255, 0))
        consigne = self.font.render("Appuie sur ESPACE pour jouer", True, (255, 255, 255))

        self.screen.blit(titre, (SCREEN_WIDTH // 2 - titre.get_width() // 2, 150))
        self.screen.blit(regles, (SCREEN_WIDTH // 2 - regles.get_width() // 2, 280))
        self.screen.blit(record, (SCREEN_WIDTH // 2 - record.get_width() // 2, 330))
        self.screen.blit(consigne, (SCREEN_WIDTH // 2 - consigne.get_width() // 2, 400))

    def draw_game(self):
        # écran de jeu
        self.screen.fill((135, 206, 235))
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.objective.image, self.objective.rect)
        self.screen.blit(self.bombe.image, self.bombe.rect)

        texte_score = self.font.render(f"Score : {self.score}", True, (255, 255, 255))
        texte_record = self.font.render(f"Record : {self.best_score}", True, (255, 255, 0))
        self.screen.blit(texte_score, (10, 10))
        self.screen.blit(texte_record, (10, 50))

        # dessiner un coeur par vie restante
        for i in range(self.lives):
            x = SCREEN_WIDTH - (i + 1) * (HEART_SIZE + 10)
            self.screen.blit(self.heart_image, (x, 10))

        aide = self.font.render("ECHAP : accueil", True, (255, 255, 255))
        self.screen.blit(aide, (10, SCREEN_HEIGHT - 40))

        if self.game_over:
            texte_fin = self.font.render("GAME OVER", True, (255, 0, 0))
            texte_rejouer = self.font.render("Appuie sur ENTREE pour rejouer", True, (255, 255, 255))
            self.screen.blit(texte_fin, (SCREEN_WIDTH // 2 - texte_fin.get_width() // 2, SCREEN_HEIGHT // 2 - 40))
            self.screen.blit(texte_rejouer, (SCREEN_WIDTH // 2 - texte_rejouer.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

    def reset(self):
        # remettre le jeu à zéro pour une nouvelle partie
        self.score = 0
        self.lives = PLAYER_LIVES
        self.game_over = False
        self.player = Player()
        self.objective = Objective()
        self.bombe = Bombe()

    def go_home(self):
        # enregistrer la partie en cours si elle n'est pas finie et si le score > 0
        if self.started and not self.game_over and self.score > 0:
            ajouter_score(self.score)
            self.best_score = max(self.best_score, meilleur_score())
        # revenir à l'écran d'accueil avec une partie neuve
        self.reset()
        self.started = False

    def run(self):
        clock = pygame.time.Clock()

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.started = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.game_over:
                    self.reset()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.go_home()

            if self.started and not self.game_over:
                self.keyboard()
                self.objective.fall()
                self.bombe.fall()
                self.check_collision()

            if self.started:
                self.draw_game()
            else:
                self.draw_home()

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()